#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils
import queue

def main():
    inp = [re.split(" bags contain |, ", line) for line in aoc_utils.input_string_list()]
    di = {line[0]: line[1:] for line in inp}
    count = 0
    for bagcolour in (i[0] for i in inp):
        if cangettoshinygold(bagcolour, di):
            count += 1
    return count

def cangettoshinygold(bagcolour, di):
    q = queue.Queue()
    q.put([bagcolour] + di[bagcolour])
    while not q.empty():
        bag = q.get()
        if "shiny gold" in ", ".join(bag[1:]):
            print(bag[0])
            return True
        else:
            if "no other bags" not in ", ".join(bag[1:]):
                for containable in bag[1:]:
                    if match := re.search(r"(?i)\d* (\w+ \w+).*", containable):
                        q.put([match.group(1)] + di[match.group(1)])
    return False

print(main())
