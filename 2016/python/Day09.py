from aoc_utils import *


def main1(inp: str) -> int:
    length = 0
    while inp != "":
        if inp[0] == "(":
            matching = inp.index(")")
            count, repeats = tuple(map(int, inp[1:matching].split("x")))
            length += count * repeats
            inp = inp[matching + count + 1 :]
        elif "(" in inp:
            first_marker = inp.index("(")
            length += first_marker
            inp = inp[first_marker:]
        else:
            length += len(inp)
            inp = ""

    return length


print(main1(input_string()))
