#!/usr/bin/python3
from parse import Result, parse

import aoc_utils


def main(a, b):
    rolls = 0
    players = [0, 0]
    players_pos = [a - 1, b - 1]
    won = False
    while not won:
        for i in range(len(players)):
            for _ in range(3):
                rolled = rolls % 100 + 1
                players_pos[i] = (players_pos[i] + rolled) % 10
                rolls += 1
            players[i] += players_pos[i] + 1
            # print(
            #     f"Player {i+1} moves to space {players_pos[i] + 1} for a total score of {players[i]}"
            # )
            if players[i] >= 1000:
                won = True
                break
    print(f"{rolls} * {min(players)} = {rolls * min(players)}")


if __name__ == "__main__":
    string = aoc_utils.input_string()
    # string = "Player 1 starting position: 4\nPlayer 2 starting position: 8"
    result = parse(
        "Player 1 starting position: {:d}\nPlayer 2 starting position: {:d}",
        string,
    )
    if not isinstance(result, Result):
        raise ValueError("Invalid input data")
    a, b = result
    main(a, b)
