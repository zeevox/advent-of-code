#!/usr/bin/python3

import itertools
from collections import Counter, defaultdict
from functools import lru_cache, partial, reduce

import more_itertools
from sortedcontainers import SortedDict, SortedList, SortedSet

import aoc_utils

sy = {"X": 1, "Y": 2, "Z": 3}

lose = {"A": "Z", "B": "X", "C": "Y"}
win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}

def main(pi):
    score = 0
    for op, you in map(str.split, pi):
        match [op, you]:
            case ["A", "Y"] | ["B", "Z"] | ["C", "X"]:
                score += sy[you] + 6
            case ["A", "Z"] | ["B", "X"] | ["C", "Y"]:
                score += 0 + sy[you]
            case ["A", "X"] | ["B", "Y"] | ["C", "Z"]:
                score += 3 + sy[you]
    return score

def mainb(pi):
    score = 0
    for op, you in map(str.split, pi):
        match you:
            case "X":
                play = lose[op]
            case "Y":
                play = draw[op]
                score += 3
            case "Z":
                play = win[op]
                score += 6
        score += sy[play]
    return score

if __name__ == "__main__":
    puzzle_input = aoc_utils.input_string_list()
    print(main(puzzle_input))
    print(mainb(puzzle_input))
