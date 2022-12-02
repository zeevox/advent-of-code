from collections import *
import itertools
import random
import re
import sys
import aoc_utils

mask = ""
mem = {}
for line in aoc_utils.input_string_list():
    i, v = line.split(" = ")
    if i == "mask":
        mask = v
    elif i[:3] == "mem":
        v = int(v)
        adr = int(i[4:-1])
        out = ""
        xs = []
        # 36 bits - hardcoded value, iterate over mask and bits simultaneously
        for i, (bv, bm) in enumerate(
            zip(list(f"{adr:b}".zfill(36)), list(mask))
        ):
            if bm == "0":
                out += bv
            elif bm == "1":
                out += "1"
            elif bm == "X":
                out += "{}"
                xs.append(i)
        # e.g. if there are 3 floating bits there are 2^3=8 combinations
        for i in range(2 ** len(xs)):
            # replace each {} with one of the bits from the binary number
            mem[int(out.format(*list(f"{i:b}".zfill(len(xs)))), 2)] = v

print(sum(mem.values()))
