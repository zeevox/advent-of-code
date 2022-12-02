from aoc_utils import *

puzzle_input = input_string()


def process(command: str, position: tuple[int, int]) -> tuple[int, int]:
    x, y = position
    match command:
        case "^":
            return (x, y + 1)
        case "v":
            return (x, y - 1)
        case ">":
            return (x + 1, y)
        case "<":
            return (x - 1, y)
    # should never reach this
    return (0, 0)


# Part 1

position: tuple[int, int] = (0, 0)
houses: set[tuple[int, int]] = {position}
for command in puzzle_input:
    position: tuple[int, int] = process(command, position)
    houses.add(position)

print(len(houses))

position_santa: tuple[int, int] = (0, 0)
position_robot: tuple[int, int] = (0, 0)

houses: set[tuple[int, int]] = {position_santa, position_robot}
for count, command in enumerate(puzzle_input):
    if count % 2 == 0:
        position_santa = process(command, position_santa)
        houses.add(position_santa)
    else:
        position_robot = process(command, position_robot)
        houses.add(position_robot)

print(len(houses))
