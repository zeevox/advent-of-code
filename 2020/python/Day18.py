#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils


def evaluate(s, part_two=False):
    vs = []
    os = []
    for c in s:
        # print(c, vs, os)
        if c.isdigit():
            vs.append(int(c))
        elif c == "(":
            os.append(c)
        elif c == ")":
            while len(os) > 0 and os[-1] != "(":
                vs.append(execute(os.pop(), vs.pop(), vs.pop()))
            os.pop()
        elif c == "*" or c == "+":
            while len(os) > 0 and has_precedence(os[-1], c, part_two):
                vs.append(execute(os.pop(), vs.pop(), vs.pop()))
            else:
                os.append(c)
    while len(os) > 0:
        vs.append(execute(os.pop(), vs.pop(), vs.pop()))
    return vs[0]


# whether o1 has greater than or equal precedence as o2
def has_precedence(o1, o2, part_two=False):
    if (part_two and o1 == "*" and o2 == "+") or o1 == "(" or o1 == ")":
        return False
    return True


def execute(o, a, b):
    if o == "*":
        return a * b
    elif o == "+":
        return a + b


# samples given on page
# print(evaluate("1 + 2 * 3 + 4  * 5 + 6"))
# print(evaluate("1 + (2 * 3) + (4 * (5 + 6))"))
# print(evaluate("2 * 3 + (4 * 5)"))
# print(evaluate("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
# print(evaluate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
# print(evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

inp = aoc_utils.input().readlines()

s = 0
for line in inp:
    s += evaluate(line)
print(s)

s = 0
for line in inp:
    s += evaluate(line, True)
print(s)
