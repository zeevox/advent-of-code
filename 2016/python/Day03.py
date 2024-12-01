import itertools

import aoc_utils
import more_itertools

triangles = [
    list(map(int, sides.strip().split())) for sides in aoc_utils.input_string_list()
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
