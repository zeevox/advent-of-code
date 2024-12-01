import itertools
from copy import deepcopy
from operator import add

import aoc_utils

dimensions = 4

# use a set instead of a list for O(1) `x in s` lookups
# https://wiki.python.org/moin/TimeComplexity
d = set()

for y, line in enumerate(aoc_utils.input_string_list()):
    for x, col in enumerate(line):
        if col == "#":
            d.add(tuple([x, y] + [0] * (dimensions - 2)))

deltas = set(itertools.product([-1, 0, 1], repeat=dimensions))
deltas.remove(tuple([0] * dimensions))


def cycle():
    data = deepcopy(d)
    changeable = set()
    for point in data:
        changeable.add(point)
        for delta in deltas:
            changeable.add(tuple(map(add, point, delta)))

    for point in changeable:
        neighbours = sum(tuple(map(add, point, delta)) in d for delta in deltas)
        if neighbours not in [2, 3]:
            data.discard(point)
        if neighbours == 3:  # and point in d:
            data.add(point)
    return data


for _ in range(6):
    d = cycle()

print(len(d))
