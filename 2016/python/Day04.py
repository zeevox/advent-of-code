from collections import Counter
from operator import itemgetter
from string import ascii_lowercase

import aoc_utils

rooms = aoc_utils.input_string_list()

count = 0
for room in rooms:
    *room, id_check = room.split("-")
    id, check = id_check.split("[")
    check = check[:-1]

    c = Counter(sorted("".join(room)))
    if check == "".join(map(itemgetter(0), c.most_common(5))):
        id = int(id)
        count += id

        deciphered = "".join(
            [
                (ascii_lowercase * 2)[ord(char) - ord("a") + id % 26]
                if char.isalpha()
                else char
                for char in " ".join(room)
            ]
        )
        if "north" in deciphered:
            print(f"Part 2: {deciphered} in {id}")

print(f"Part 1: {count}")
