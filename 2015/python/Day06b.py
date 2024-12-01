import itertools
from collections import defaultdict

from aoc_utils import input_string_list

instructions = input_string_list()

lights: defaultdict[tuple[int, int], int] = defaultdict(int)


def get_coordinates(corner1: tuple[int, int], corner2: tuple[int, int]):
    yield from itertools.product(
        range(corner1[0], corner2[0] + 1), range(corner1[1], corner2[1] + 1)
    )


def parse_coords(coord_string: str) -> tuple[int, int]:
    x, y = coord_string.split(",")
    return (int(x), int(y))


for instruction in instructions:
    match instruction.split():
        case ["turn", "on", corner1, "through", corner2]:
            for coord in get_coordinates(parse_coords(corner1), parse_coords(corner2)):
                lights[coord] += 1
        case ["toggle", corner1, "through", corner2]:
            for coord in get_coordinates(parse_coords(corner1), parse_coords(corner2)):
                lights[coord] += 2
        case ["turn", "off", corner1, "through", corner2]:
            for coord in get_coordinates(parse_coords(corner1), parse_coords(corner2)):
                lights[coord] = max(lights[coord] - 1, 0)

print(sum(lights.values()))
