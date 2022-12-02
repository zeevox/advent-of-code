from collections import *
import itertools
import random
import re
import sys
import aoc_utils
import queue


def main():
    inp = [
        re.split(" bags contain |, ", line)
        for line in aoc_utils.input_string_list()
    ]
    return bagscontain("shiny gold", inp)


def bagscontain(bagcolour, inp):
    di = {line[0]: line[1:] for line in inp}
    count = 0
    bag = [bagcolour] + di[bagcolour]
    if "no other bags" not in ", ".join(bag[1:]):
        subbags = []
        for containable in bag[1:]:
            if match := re.search(r"(?i)\d* (\w+ \w+).*", containable):
                count += int(containable.split(" ")[0]) * (
                    1 + bagscontain(match[1], inp)
                )
                subbags.append([match[1]] + di[match[1]])
    return count


print(main())
