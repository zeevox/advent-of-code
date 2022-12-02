import aoc_utils


def maina(puzzle_input: str) -> int:
    floor = 0
    for bracket in puzzle_input:
        if bracket == "(":
            floor += 1
        elif bracket == ")":
            floor -= 1
    return floor


def mainb(puzzle_input: str) -> int:
    floor = 0
    for index, bracket in enumerate(puzzle_input):
        if floor < 0:
            return index
        if bracket == "(":
            floor += 1
        elif bracket == ")":
            floor -= 1
    raise ValueError("Santa never goes below the ground floor")


if __name__ == "__main__":
    puzzle_input = aoc_utils.input_string()
    print(maina(puzzle_input))
    print(mainb(puzzle_input))
