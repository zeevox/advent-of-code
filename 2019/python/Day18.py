#!/usr/bin/python3

from collections import *
import itertools
import typing
import networkx as nx
import numpy as np
from queue import Queue
from collections.abc import Iterable


def print_grid(grid: typing.Union[np.ndarray, list[list[object]]]) -> None:
    """Prints a 2D array as a grid"""
    print(*map("".join, grid), sep="\n")


def get_neighbours(
    point: list[int],
    include_diagonals: bool = True,
    exclude_p: bool = True,
    shape: list[int] = None,
):
    """
    Yield the coordinates of points directly (or diagonally) adjacent to a given point, excluding points that are out of bounds
    """
    print(*itertools.product((-1, 0, 1), repeat=len(point)))
    print(*itertools.permutations([1] + [0] * (len(point) - 2)))


def get_neighbours2(
    p: list[int],
    include_diagonals: bool = True,
    exclude_p: bool = True,
    shape: list[int] = None,
):
    """adapted from https://stackoverflow.com/a/34908879"""

    ndim = len(p)

    # generate an (m, ndims) array containing all strings over the alphabet {0, 1, 2}:
    offset_idx = np.indices((3,) * ndim).reshape(ndim, -1).T

    # use these to index into np.array([-1, 0, 1]) to get offsets
    offsets = np.r_[-1, 0, 1].take(offset_idx)
    print(np.r_[-1, 0, 1])
    print(offset_idx)
    print(offsets)

    # generate all possible offsets

    # optional: exclude offsets of 0, 0, ..., 0 (i.e. p itself)
    if exclude_p:
        offsets = offsets[np.any(offsets, 1)]

    neighbours = p + offsets  # apply offsets to p

    # optional: exclude out-of-bounds indices
    if shape is not None:
        valid = np.all(
            (neighbours < np.array(shape)) & (neighbours >= 0), axis=1
        )
        neighbours = neighbours[valid]

    return neighbours


def main(puzzle_input: str) -> None:
    grid = np.array(list(map(list, puzzle_input.splitlines())), ndmin=2)
    entry_point = next(zip(*np.where(grid == "@")))
    print_grid(grid)
    to_visit = Queue()
    to_visit.put(entry_point)
    print(grid.shape)
    print(
        *map(
            tuple,
            filter(
                lambda point: grid[tuple(point)] != "#",
                get_neighbours(entry_point, shape=grid.shape),
            ),
        )
    )


maps = [
    """#########
#b.A.@.a#
#########
""",
    """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
""",
    """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################
""",
    """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################
""",
    """########################
#@..............ac.GI.b#
###d#e#f################
###A#B#C################
###g#h#i################
########################
""",
]

if __name__ == "__main__":
    main(maps[0])
