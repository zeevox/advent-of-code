#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils


def main(dx, dy):
    x, y = 0, 0
    map = aoc_utils.input_string_list()
    trees = 0
    while y < len(map):
        if map[y][x % len(map[y])] == "#":
            trees += 1
        x += dx
        y += dy
    return trees


print(main(3, 1))
print(main(1, 1) * main(3, 1) * main(5, 1) * main(7, 1) * main(1, 2))
