#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils

if __name__ == "__main__":
    # nine slots for fish aged 0-8
    fishes = deque([0] * 9)
    # each slot is a counter of the number fish of that age
    for fish in map(int, aoc_utils.input_string_list()[0].split(",")):
        fishes[fish] += 1
    # repeat the process lots of times (80 for first part, 256 for second)
    for i in range(256):
        # those fish that were aged zero were at the leftmost end of the list
        fishes_to_reset = fishes.popleft()
        # these fish are now aged six and their children aged eight (logik)
        fishes[6] += fishes_to_reset
        fishes.append(fishes_to_reset)
    # all we need is the total number of such fish
    print(sum(fishes))
