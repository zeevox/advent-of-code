from collections import *
import itertools
import random
import re
import sys
import aoc_utils

ins = aoc_utils.input_string_list()
sx, sy, d = 0, 0, 90
wx, wy = 10, 1
for i in ins:
    c = i[0]
    n = int(i[1:])
    if c == "N":
        wy += n
    elif c == "S":
        wy -= n
    elif c == "E":
        wx += n
    elif c == "W":
        wx -= n
    elif (c == "L" and n == 90) or (c == "R" and n == 270):
        wx, wy = -wy, wx
    elif c in ["L", "R"] and n == 180:
        wx, wy = -wx, -wy
    elif (c == "L" and n == 270) or (c == "R" and n == 90):
        wx, wy = wy, -wx
    elif c == "F":
        sx += n * wx
        sy += n * wy
    print(sx, sy, d)
print(abs(sx) + abs(sy))
