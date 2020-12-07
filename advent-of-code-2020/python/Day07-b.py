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
    return bagscontain("shiny gold", inp)

def bagscontain(bagcolour, inp):
    di = {line[0]: line[1:] for line in inp}
    #print(*inp, sep="\n")
    count = 0
    bag = [bagcolour] + di[bagcolour]
    subbags = []
    if "no other bags" not in ", ".join(bag[1:]):
        for containable in bag[1:]:
            if match := re.search(r"(?i)\d* (\w+ \w+).*", containable):
                #print(match.group(1))
                count += int(containable.split(" ")[0]) * (1 + bagscontain(match.group(1), inp))
                subbags.append([match.group(1)] + di[match.group(1)])
    return count
    #count += sum([bagscontain(])
    #q = queue.Queue()
    #q.put([bagcolour] + di[bagcolour])
    #while not q.empty():
        #print(list(q.queue))
        #bag = q.get()
        #print(bag)
        #print(bag, ", ".join(bag[1:]))
        #if "shiny gold" in ", ".join(bag[1:]):
        #    print(bag[0])
        #    return True
        #else:
    #return False

print(main())
