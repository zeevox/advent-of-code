import itertools
from aoc_utils import *

instructions = input_string_list()

lights: set[tuple[int, int]] = set()


def parse_coords(coord_string: str) -> tuple[int, int]:
    x, y = coord_string.split(",")
    return (int(x), int(y))


for instruction in instructions:
    match instruction.split():
        case ["turn", "on", corner1, "through", corner2]:
            for coord in gen_rectangle_coords(
                parse_coords(corner1), parse_coords(corner2)
            ):
                lights.add(coord)
        case ["toggle", corner1, "through", corner2]:
            for coord in gen_rectangle_coords(
                parse_coords(corner1), parse_coords(corner2)
            ):
                if coord in lights:
                    lights.discard(coord)
                else:
                    lights.add(coord)
        case ["turn", "off", corner1, "through", corner2]:
            for coord in gen_rectangle_coords(
                parse_coords(corner1), parse_coords(corner2)
            ):
                lights.discard(coord)

print(len(lights))
