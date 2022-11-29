#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils

"""matching bracket-pairs to avoid using if-else statements"""
matches = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
"""syntax checker points map"""
points_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
"""autocomplete points map"""
ac_points_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def main(lines: list[str]):
    points = 0
    scores = []
    for line in lines:
        stack = []
        for i, character in enumerate(line):
            # iterate through until an unmatched bracket is found
            if character in matches.keys():
                # if the character is an open bracket, add it to the stack
                stack.append(character)
            elif character in matches.values():
                # if the character is a close bracket, pop the stack
                if matches[stack.pop()] != character:
                    print(f"Unmatched bracket: {character} at position {i}")
                    points += points_map[character]
                    break
        # use the wonderful for-else construct for cases where the line is not corrupted
        else:
            score = 0
            for unmatched_bracket in stack[::-1]:
                score = score * 5 + ac_points_map[matches[unmatched_bracket]]
            scores.append(score)

    scores.sort()
    print(f"Total points: {points}")
    print(f"Middle score: {scores[len(scores) // 2]}")


if __name__ == "__main__":
    main(aoc_utils.input_string_list())
