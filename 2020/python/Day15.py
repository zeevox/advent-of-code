#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils

li = [1, 0, 15, 2, 10, 13]
freq = {x: [i + 1, i + 1] for i, x in enumerate(li)}

counter = len(li) + 1
last = li[counter - 2]
while counter <= 30000000:
    p = freq[last]
    v = 0 if p[0] == p[1] else p[1] - p[0]
    last = v
    freq[v] = [freq.get(v, [counter])[-1], counter]
    # just to get an idea of how much progress we were making
    # print(counter/30000000*100)
    counter += 1

print(last)
