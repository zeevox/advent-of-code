#!/usr/bin/python3

import functools
import operator
from typing import Generator
import aoc_utils


def gen_adjacent_coords(
    point: tuple[int, int]
) -> Generator[tuple[int, int], None, None]:
    for vertical_offset in [-1, 0, 1]:
        for horizontal_offset in [-1, 0, 1]:
            yield (point[0] + horizontal_offset, point[1] + vertical_offset)


def bounds(lit_pixels: set[tuple[int, int]]) -> tuple[int, int, int, int]:
    return (
        min(map(operator.itemgetter(0), lit_pixels)),
        max(map(operator.itemgetter(0), lit_pixels)),
        min(map(operator.itemgetter(1), lit_pixels)),
        max(map(operator.itemgetter(1), lit_pixels)),
    )


def main(
    algorithm: dict[int, int], lit_pixels: set[tuple[int, int]], infinite_lit: bool
) -> set[tuple[int, int]]:
    min_x, max_x, min_y, max_y = bounds(lit_pixels)
    new_lit_pixels = set()
    for y in range(min_y - 2, max_y + 3):
        for x in range(min_x - 2, max_x + 3):
            index = functools.reduce(
                lambda acc, neighbour: (acc * 2)
                | int(neighbour in lit_pixels)
                | (
                    infinite_lit
                    and (
                        neighbour[0] < min_x
                        or neighbour[0] > max_x
                        or neighbour[1] < min_y
                        or neighbour[1] > max_y
                    )
                ),
                gen_adjacent_coords((x, y)),
                0,
            )
            new_value = algorithm[index]
            if new_value == 1:
                new_lit_pixels.add((x, y))
    return new_lit_pixels, not infinite_lit


if __name__ == "__main__":
    algorithm_str, image_str = aoc_utils.input_block_list()

    algorithm = dict((i, int(v == "#")) for i, v in enumerate(algorithm_str))

    lit_pixels = set()
    for y, row in enumerate(image_str.splitlines()):
        for x, value in enumerate(row):
            if value == "#":
                lit_pixels.add((x, y))

    infinite_lit = False
    for _ in range(2):
        lit_pixels, infinite_lit = main(algorithm, lit_pixels, infinite_lit)

    print(len(lit_pixels))

    for _ in range(48):
        lit_pixels, infinite_lit = main(algorithm, lit_pixels, infinite_lit)

    print(len(lit_pixels))
