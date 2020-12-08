#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils

def main():
    acc = 0
    pointer = 0
    pointers = []
    inp = aoc_utils.input_string_list()
    while pointer < len(inp) and pointer not in pointers:
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

print(main())
