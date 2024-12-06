import collections
import datetime
import json
import os
import timeit

import humanize
import pandas
import pytz
import requests_cache
from requests.structures import CaseInsensitiveDict

session = requests_cache.CachedSession(
    "aoc_cache",
    use_cache_dir=True,
    cache_control=True,
    expire_after=datetime.timedelta(minutes=15),
)


def get_session_cookie() -> str:
    """
    Get the session cookie for the user.
    :return: The session cookie.
    """
    home = os.path.expanduser("~")
    cookie_file = home + "/.aocdlconfig"

    if not os.path.isfile(cookie_file):
        print("Error: No cookie file found.")
        exit(1)

    with open(cookie_file) as f:
        return json.load(f)["session-cookie"]


def get_aoc_leaderboard(year: int = 2021, leaderboard_id: int = 805152) -> dict:
    """
    Get the official private leaderboard from Advent of Code.
    """

    response = session.get(
        f"https://adventofcode.com/{year}/leaderboard/private/view/{leaderboard_id}.json",
        headers=CaseInsensitiveDict({"cookie": f"session={get_session_cookie()}"}),
    )

    try:
        return json.loads(response.text)
    except json.decoder.JSONDecodeError:
        print("<code>Error: Invalid response from AoC server.</code>")
        print(f"<pre>{response}\n{response.text}</pre>")
        exit(1)


def is_star_on_day(ts: int, day: int, year: int = 2021) -> bool:
    """whether or not the star was gotten on the given day"""
    est = pytz.timezone("US/Eastern")
    return (
        est.localize(datetime.datetime(year, 12, day, 0, 0, 0))
        <= pytz.utc.localize(datetime.datetime.fromtimestamp(ts))
        <= est.localize(datetime.datetime(year, 12, day, 23, 59, 59))
    )


def stars_for_each_day(
    days_data: dict[int, dict[str, dict[str, int]]], year: int = 2021
) -> dict[int, int]:
    """Number of stars that the user earned on each day of the challenge"""
    user_data = collections.defaultdict(int)
    cumulative_delta = datetime.timedelta(0)
    no_of_full_days = 0
    for day, stars in days_data.items():
        for starno, star in stars.items():
            if is_star_on_day(star["get_star_ts"], int(day), year):
                user_data[day] += 2
            else:
                user_data[day] += 1
            if starno == "2":
                cumulative_delta += datetime.datetime.fromtimestamp(
                    star["get_star_ts"]
                ) - datetime.datetime.fromtimestamp(stars["1"]["get_star_ts"])
                no_of_full_days += 1
    return user_data, (
        cumulative_delta / no_of_full_days
        if no_of_full_days > 0 and cumulative_delta > datetime.timedelta(0)
        else None
    )


def points_for_user(user_data: dict[int, int]) -> int:
    """Total points earned by the user"""
    return sum(user_data.values())


autonyms = {
    "bluewhale64": "Noah Whale",
    "Charles C": "Charles Calzia",
    "egkoppel": "Eliyahu Gluschove-Koppel",
    "GDBWN V": "George Niedringhaus",
    "Liftyee": "Victor Liu",
    "Sid": "Sid Chaudhary",
    "xXSandro-EnukidzeXx": "Sandro Enukidze",
    "Christopher Harrison": "Dr Harrison",
    "Steven Carter": "Mr Carter",
    "zacstalbow": "Zac Stalbow",
    "Vxtr10": "Victor Shao",
    "BoomydayCoder": "Adavya",
}

years = {
    "Arnav Sharma": "L8th",
    "Sid Chaudhary": "4th",
    "Anango Prabhat": "4th",
    "Haolin Zhao": "6th",
    "Rex Weber-Brown": "6th",
    "Dingyan Zhang": "L8th",
    "Rahul Marchand": "L8th",
    "Charles Calzia": "L8th",
    "Eliyahu Gluschove-Koppel": "L8th",
    "Oliver Hiorns": "L8th",
    "Jude Carter": "L8th",
    "Victor Liu": "6th",
    "Vilhelm Kjellberg": "L8th",
    "Aarav Kushagra": "4th",
    "Stefano Frigo": "L8th",
    "Harry Rimmer": "L8th",
    "George Niedringhaus": "L8th",
    "Noah Whale": "L8th",
    "Kiminao Usami": "L8th",
    "Yuvraj D": "U8th",
    "Timothy Langer": "U8th",
    "Elias Fizesan": "U8th",
    "Lorenzo Usai": "U8th",
    "Max Bowman": "U8th",
    "Dhruv Pattem": "U8th",
    "Jacob Hill": "U8th",
    "Sandro Enukidze": "U8th",
    "Jim Roberts": "U8th",
    "Vivek Aggala": "U8th",
    "Dr Harrison": "---",
    "Mr Carter": "---",
    "Zak Farazi": "L8th",
    "Shyam Thobhani": "6th",
    "Henry Squire": "L8th",
    "Vikram Bhamre": "L8th",
    "Rakan Sharaiha": "6th",
    "Harrish Shivakumar": "6th",
    "Ian Averre": "6th",
    "Laith Gordon": "U8th",
    "Thomas Stanger": "U8th",
    "Cameron Soo": "U8th",
    "Elijah Patterson": "L8th",
    "Zac Stalbow": "U8th",
    "Victor Shao": "L8th",
    "Victor Moreno": "L8th",
    "Ethan Lim": "U8th",
    "Chongyang Cao": "6th",
    "Sean Chong": "L8th",
    "Oliver Edmond": "L8th",
    "Owais (Gabriel) Hussain": "6th",
    "Kimi Liu": "L8th",
    "Daniel Hou": "L8th",
    "Alexander Rathour": "6th",
    "Adavya": "4th",
    "Royal Sule": "L8th",
    "Rory McDowell": "U8th",
    "Rehman Oomer": "U8th",
}


def get_custom_leaderboard() -> pandas.DataFrame:
    """Custom leaderboard that awards points for completing the challenge on the day of the star"""
    aoc_leaderboard = get_aoc_leaderboard()["members"].values()
    for member in aoc_leaderboard:
        if member["local_score"] == 0:
            continue
        if member["name"] in autonyms:
            member["name"] = autonyms[member["name"]]
        for names, yeargroup in years.items():
            if member["name"] in names:
                member["yeargroup"] = yeargroup
        if "yeargroup" not in member:
            member["yeargroup"] = "???"

    return pandas.DataFrame(
        [
            [
                member["name"],
                points_for_user(
                    (data := stars_for_each_day(member["completion_day_level"]))[0]
                ),
                member["yeargroup"],
                data[1],
            ]
            for member in aoc_leaderboard
            if member["local_score"] != 0
        ],
        columns=["Name", "Score", "Year", "Avg Delta Time"],
    )


def main():  #
    leaderboard = get_custom_leaderboard()
    leaderboard = leaderboard.sort_values(
        by=["Score", "Avg Delta Time"], ascending=[False, True]
    )
    leaderboard["Avg Delta Time"] = leaderboard["Avg Delta Time"].map(
        lambda dt: "---"
        if pandas.isnull(dt)
        else humanize.precisedelta(
            dt, suppress=["days"], minimum_unit="seconds", format="%0d"
        )
    )
    last_refresh = next(
        response.created_at for response in session.cache.responses.values()
    )
    print(
        f"<p>Last refreshed {humanize.naturaldelta(last_refresh)} ago (cached for 15 minutes)</p>"
    )
    print(leaderboard.to_html(index=False, classes="sortable"))


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    load_time = humanize.precisedelta(
        datetime.timedelta(seconds=timeit.default_timer() - start_time),
        minimum_unit="milliseconds",
    )
    print(f"<small>Load time: {load_time}</small>")
