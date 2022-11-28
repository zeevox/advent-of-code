#!/usr/bin/python3

import itertools
import more_itertools

with open(f"2016/inputs/03.txt", "r") as f:
    triangles = [
        list(map(int, sides.strip().split())) for sides in f.read().strip().splitlines()
    ]

count = 0
for sides in triangles:
    for perm_sides in itertools.permutations(sides):
        if sum(perm_sides[:2]) <= perm_sides[2]:
            break
    else:
        count += 1

print(count)

count = 0
for chunk in more_itertools.chunked(triangles, 3):
    for triangle in zip(*chunk):
        for perm_sides in itertools.permutations(triangle):
            if sum(perm_sides[:2]) <= perm_sides[2]:
                break
        else:
            count += 1

print(count)
