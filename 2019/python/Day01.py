from collections import *
import itertools
import random
import re
import sys
import aoc_utils

# Part 1
ms = aoc_utils.input_int_list()
print(sum(map(lambda m: (m // 3) - 2, ms)))


def fuel(n):
    return max(0, (n // 3) - 2)


s = 0
for m in ms:
    f = fuel(m)
    while f > 0:
        s += f
        f = fuel(f)

print(s)
