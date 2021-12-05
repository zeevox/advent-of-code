#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils


def has_double(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


def has_only_double(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            if i >= 1 and s[i - 1] != s[i] or i == 0:
                if i < len(s) - 2 and s[i + 2] != s[i] or i == len(s) - 2:
                    return True
    return False


def no_decreasing(s):
    for i in range(len(s) - 1):
        if int(s[i]) > int(s[i + 1]):
            return False
    return True


def main(start: int, end: int):
    print(
        len(
            list(
                filter(
                    lambda x: has_double(x) and no_decreasing(x),
                    map(str, range(start, end + 1)),
                )
            )
        )
    )

    print(
        len(
            list(
                filter(
                    lambda x: has_only_double(x) and no_decreasing(x),
                    map(str, range(start, end + 1)),
                )
            )
        )
    )


main(387638, 919123)
