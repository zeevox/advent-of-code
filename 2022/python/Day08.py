import itertools
import math

from aoc_utils import *


def transposed(grid: list[list[int]]):
    return list(zip(*grid))


grid = [[int(char) for char in line] for line in input_string_list()]
gridt = transposed(grid)


def is_visible(xy: tuple[int, int]):
    global grid, gridt
    x, y = xy
    maxes = [
        max([-1] + grid[y][:x]),
        max([-1] + grid[y][x + 1 :]),
        max((-1,) + gridt[x][:y]),
        max((-1,) + gridt[x][y + 1 :]),
    ]

    return min(maxes) < grid[y][x]


def countwhile(func, it) -> int:
    count = 0
    for item in it:
        count += 1
        if not func(item):
            break
    return count


def scenic_score(xy: tuple[int, int]) -> int:
    global grid, gridt
    x, y = xy
    tree = grid[y][x]

    def shorter(other):
        return other < tree

    scenicities = [
        countwhile(shorter, grid[y][:x][::-1]),
        countwhile(shorter, grid[y][x + 1 :]),
        countwhile(shorter, gridt[x][:y][::-1]),
        countwhile(shorter, gridt[x][y + 1 :]),
    ]
    return math.prod(scenicities)


if __name__ == "__main__":
    print(
        sum(
            1
            for xy in itertools.product(range(len(grid[0])), range(len(grid)))
            if is_visible(xy)
        )
    )

    print(
        max(
            scenic_score(xy)
            for xy in itertools.product(range(len(grid[0])), range(len(grid)))
        )
    )
