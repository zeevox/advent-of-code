#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils

def main(parttwo = False):
    inp = aoc_utils.input_block_list()
    count = 0
    for group in inp:
        if parttwo:
            splitgroup = aoc_utils.filter_empty(group.split("\n"))
            li1 = set(splitgroup[0])
            for line in splitgroup[1:]:
                li1 = li1.intersection(set(line))
            count += len(li1)
        else:
            group = group.replace("\n", "")
            count += len(set(group))
    return count
print(main())
print(main(True))
