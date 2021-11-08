#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils


def intcode(inp, noun, verb):
    xs = list(map(int, inp.split(',')))

    xs[1], xs[2] = noun, verb

    i = 0
    while True:
        if xs[i] == 1:
            xs[xs[i+3]] = xs[xs[i+1]] + xs[xs[i+2]]
            i += 4
        elif xs[i] == 2:
            xs[xs[i+3]] = xs[xs[i+1]] * xs[xs[i+2]]
            i += 4
        elif xs[i] == 99:
            break
    return xs

# should print 3500
#print(intcode("1,9,10,3,2,3,11,0,99,30,40,50"))

# Part 1
print(intcode(aoc_utils.input().read(), 12, 2)[0])

# Part 2
for n, v in itertools.product(range(100), range(100)):
    if intcode(aoc_utils.input().read(), n, v)[0] == 19690720:
        print(100 * n + v)
        break

