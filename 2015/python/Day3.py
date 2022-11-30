#!/usr/bin/python3

with open("../inputs/3.txt", "r") as file:
    puzzle_input = file.read()


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


### Part 1

houses: set[tuple[int, int]] = set()
position: tuple[int, int] = (0, 0)
houses.add(position)

for command in puzzle_input:
    position: tuple[int, int] = process(command, position)
    houses.add(position)

print(len(houses))

### Part 2

houses: set[tuple[int, int]] = set()
position_santa: tuple[int, int] = (0, 0)
position_robot: tuple[int, int] = (0, 0)

houses.add(position_santa)
houses.add(position_robot)  # for completeness

for count, command in enumerate(puzzle_input):
    if count % 2 == 0:
        position_santa = process(command, position_santa)
        houses.add(position_santa)
    else:
        position_robot = process(command, position_robot)
        houses.add(position_robot)

print(len(houses))
