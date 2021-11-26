#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils
from copy import deepcopy


def main(rs):
    ors = deepcopy(rs)
    for y, row in enumerate(ors):
        for x, seat in enumerate(row):
            if ors[y][x] == ".":
                continue
            ajs = adj_seats(x, y, ors)
            if ors[y][x] == "L" and ajs.count("#") == 0:
                rs[y][x] = "#"
                continue
            if ors[y][x] == "#" and ajs.count("#") >= 4:
                rs[y][x] = "L"
                continue
    if rs == ors:
        return rs
    else:
        # print(*rs, sep="\n")
        return main(rs)


def adj_seats(x, y, rs):
    ajs = []
    rows, cols = len(rs), len(rs[0])
    if x > 0:
        ajs.append(rs[y][x - 1])
    if x + 1 < cols:
        ajs.append(rs[y][x + 1])
    if y > 0:
        ajs.append(rs[y - 1][x])
    if y + 1 < rows:
        ajs.append(rs[y + 1][x])
    if x > 0 and y > 0:
        ajs.append(rs[y - 1][x - 1])
    if x + 1 < cols and y > 0:
        ajs.append(rs[y - 1][x + 1])
    if x + 1 < cols and y + 1 < rows:
        ajs.append(rs[y + 1][x + 1])
    if x > 0 and y + 1 < rows:
        ajs.append(rs[y + 1][x - 1])
    return ajs


rs = [list(s) for s in aoc_utils.input_string_list()]
rows, cols = len(rs[0]), len(rs)

# print(*(r := main(rs)), sep="\n")
main(rs)
print("".join(["".join(s) for s in rs]).count("#"))
