#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils

def calculate(inp, acc = 0, pointer = 0):
    pointers = []
    while pointer < len(inp):
        if pointer in pointers:
            return None # infinite loop
        kv = inp[pointer].split()
        pointers.append(pointer)
        if kv[0] == "acc":
            acc += int(kv[1])
            pointer += 1
        elif kv[0] == "jmp":
            pointer += int(kv[1])
        else:
            pointer += 1
    return acc

inp = aoc_utils.input_string_list()

print(calculate(inp))

for line_no in range(len(inp)):
    command = inp[line_no].split()[0]
    if command == "acc":
        continue
    inp[line_no] = ("jmp" if command == "nop" else "nop") + inp[line_no][3:]
    x = calculate(inp)
    if x is not None:
        print(x, line_no)
        exit()
    else:
        # undo
        inp[line_no] = command + inp[line_no][3:]
