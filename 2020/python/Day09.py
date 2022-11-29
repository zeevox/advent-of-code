#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils

"""
My answers were
    Part A: 167829540
    Part B: 28045630
"""

inp = aoc_utils.input_int_list()

preamble = 25
"""
Finding all the sums of two numbers in the `preamble` length subarray

Create a dictionary, in which keys are the sums of two numbers and the value
is a tuple containing the indices of the two numbers that produced this sum.

Although there are two nested for loops, it turns out as O(preamble * n),
which is essentially O(n).
"""
di = {}
for i in range(preamble, len(inp)):
    for j in range(i - preamble, i):
        di[inp[i] + inp[j]] = (i, j)

invalid_num = -1
for n in range(preamble, len(inp)):
    # the commented code was necessary to get the sample input working
    # but for the actual input it broke my code?!?
    # not sure what went wrong there
    if (
        x := di.get(inp[n], -1)
    ) == -1:  # or not all([i in range(n - preamble, n) for i in x]):
        invalid_num = inp[n]

print("No such invalid number" if invalid_num == -1 else invalid_num)
"""
# Finding the sum of a subarray

Use two pointers, that point to the first and last value (or in this case
slicepoint) of the subarray. On each turn, the left pointer moves one step
to the right and right pointer moves to the right as long as the resulting
subarray sum is at most our target value. If the sum is our target value
then we have found the solution.
"""

left, right = 0, 0

s = 0
while True:
    if s == invalid_num:
        break
    elif s + inp[right] > invalid_num:
        left += 1
        if left == right:
            right += 1
    else:
        right += 1
    s = sum(inp[left:right])

print(min(subarray := inp[left:right]) + max(subarray))
