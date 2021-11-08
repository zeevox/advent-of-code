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
            if ors[y][x] == '.':
                continue
            ajs = adj_seats(x,y,ors)
            if ors[y][x] == 'L' and ajs.count('#') == 0:
                rs[y][x] = '#'
                continue
            if ors[y][x] == '#' and ajs.count('#') >= 5:
                rs[y][x] = 'L'
                continue
    if rs == ors:
        return rs
    else:
        #print(*rs, sep="\n")
        return main(rs)

def adj_seats(x, y, rs):
    ajs = []
    rows, cols = len(rs), len(rs[0])
    if x > 0:
        sx, sy = x-1, y
        s = rs[sy][sx]
        while s == '.' and sx > 0:
            sx -= 1
            s = rs[sy][sx]
        if s != '.':
            ajs.append(s)
    if x + 1 < cols:
        sx, sy = x+1, y
        s = rs[sy][sx]
        while s == '.' and sx + 1 < cols:
            sx += 1
            s = rs[sy][sx]
        if s != '.':
            ajs.append(s)
    if y > 0:
        sx, sy = x, y-1
        s = rs[sy][sx]
        while s == '.' and sy > 0:
            sy -= 1
            s = rs[sy][sx]
        if s != '.':
            ajs.append(s)
    if y + 1 < rows:
        sx, sy = x, y+1
        s = rs[sy][sx]
        while s == '.' and sy + 1 < rows:
            sy += 1
            s = rs[sy][sx]
        if s != '.':
            ajs.append(s)
    if x > 0 and y > 0:
        sx, sy = x-1, y-1
        s = rs[sy][sx]
        while s == '.' and sx > 0 and sy > 0:
            sx -= 1
            sy -= 1
            s = rs[sy][sx]
        if s != '.':
            ajs.append(s)
    if x + 1 < cols and y > 0:
        sx, sy = x+1, y-1
        s = rs[sy][sx]
        while s == '.' and sx + 1 < cols and sy > 0:
            sx += 1
            sy -= 1
            s = rs[sy][sx]
        if s != '.':
            ajs.append(s)
    if x + 1 < cols and y + 1 < rows:
        sx, sy = x+1, y+1
        s = rs[sy][sx]
        while s == '.' and sx + 1 < cols and sy + 1 < rows:
            sx += 1
            sy += 1
            s = rs[sy][sx]
        if s != '.':
            ajs.append(s)
    if x > 0 and y + 1 < rows:
        sx, sy = x-1, y+1
        s = rs[sy][sx]
        while s == '.' and sx > 0 and sy + 1 < rows:
            sx -= 1
            sy += 1
            s = rs[sy][sx]
        if s != '.':
            ajs.append(s)
    return ajs

ts = [".##.##.",
"#.#.#.#",
"##...##",
"...L...",
"##...##",
"#.#.#.#",
".##.##."]

#test that adj_seats works
#print(adj_seats(3,3,ts))


rs = [list(s) for s in aoc_utils.input_string_list()]
rows, cols = len(rs[0]), len(rs)

#print(*(r := main(rs)), sep="\n")
main(rs)
print("".join(["".join(s) for s in rs]).count("#"))
