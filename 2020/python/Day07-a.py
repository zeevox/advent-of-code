#!/usr/bin/python3

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
    di = {line[0]: line[1:] for line in inp}
    return sum(
        bool(route_possible(start_colour, "shiny gold", di))
        for start_colour in (i[0] for i in inp)
    )


def route_possible(start_colour, end_colour, di):
    q = queue.Queue()
    q.put([start_colour] + di[start_colour])
    while not q.empty():
        bag = q.get()
        if end_colour in ", ".join(bag[1:]):
            return True
        if "no other bags" not in ", ".join(bag[1:]):
            for containable in bag[1:]:
                # this regex gets the bag colour, which is always two words long.
                if match := re.search(r"(?i)\d* (\w+ \w+).*", containable):
                    q.put([match[1]] + di[match[1]])
    return False


print(main())
