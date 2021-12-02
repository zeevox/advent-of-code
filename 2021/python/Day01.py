#!/usr/bin/python3

import itertools
import random
import re
import sys
from collections import *

import aoc_utils


def main(xs: list[int]) -> int:
    print(sum(x < y for x, y in zip(xs, xs[3:])))
    print(sum([1 for i, num in enumerate(xs[3:]) if num > xs[i]]))

    count = 0
    for i in range(2, len(xs) - 1):
        if sum(xs[i - 1 : i + 2]) > sum(xs[i - 2 : i + 1]):
            count += 1
    return count


if __name__ == "__main__":
    print(main([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))
    print(main(aoc_utils.input_int_list()))
