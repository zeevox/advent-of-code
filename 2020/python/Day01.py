#!/usr/bin/python3

from collections import *
import itertools
import random
import sys
import aoc_utils


def main(target):
    array = [False] * target
    for x in aoc_utils.input_int_list():
        if x < target:
            array[x] = True
    return next(
        (
            (i, target - i)
            for i in range(target)
            if array[i] and array[target - i]
        ),
        [],
    )


def three():
    for x in aoc_utils.input_int_list():
        complements = main(2020 - x)
        if len(complements) <= 0:
            continue
        if x + complements[0] + complements[1] == 2020 and not (
            complements[0] == x or complements[1] == x
        ):
            return x * complements[0] * complements[1]


output = main(2020)
print(output[0] * output[1])
print(three())
