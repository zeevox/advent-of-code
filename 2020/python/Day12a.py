from collections import *
import itertools
import random
import re
import sys
import aoc_utils

ins = aoc_utils.input_string_list()
x, y, d = 0, 0, 90
for i in ins:
    c = i[0]
    n = int(i[1:])
    if c == "N":
        y += n
    elif c == "S":
        y -= n
    elif c == "E":
        x += n
    elif c == "W":
        x -= n
    elif c == "L":
        d -= n
        if d < 0:
            d += 360
    elif c == "R":
        d += n
        if d >= 360:
            d -= 360
    elif c == "F":
        if d == 0:
            y += n
        elif d == 90:
            x += n
        elif d == 180:
            y -= n
        elif d == 270:
            x -= n
    print(x, y, d)
print(abs(x) + abs(y))
