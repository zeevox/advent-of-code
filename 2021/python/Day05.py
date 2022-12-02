import re
from collections import defaultdict

from aoc_utils import *


def main(lines: list[str]) -> None:
    grid: dict[tuple[int, int], int] = defaultdict(int)
    lines_parsed = [list(map(int, re.findall(r"\d+", line))) for line in lines]

    for x1, y1, x2, y2 in lines_parsed:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[(x, y1)] += 1

    print(sum(v >= 2 for v in grid.values()))

    for x1, y1, x2, y2 in lines_parsed:
        if abs(x1 - x2) != abs(y1 - y2):
            continue

        if x1 < x2 and y1 < y2:
            for x, y in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
                grid[(x, y)] += 1
        elif x1 < x2 and y1 > y2:
            for x, y in zip(range(x1, x2 + 1), range(y1, y2 - 1, -1)):
                grid[(x, y)] += 1
        elif x1 > x2 and y1 < y2:
            for x, y in zip(range(x1, x2 - 1, -1), range(y1, y2 + 1)):
                grid[(x, y)] += 1
        elif x1 > x2 and y1 > y2:
            for x, y in zip(range(x1, x2 - 1, -1), range(y1, y2 - 1, -1)):
                grid[(x, y)] += 1

    print(sum(v >= 2 for v in grid.values()))


if __name__ == "__main__":
    main(input_string_list())
