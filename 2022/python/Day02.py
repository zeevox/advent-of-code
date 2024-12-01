import aoc_utils

scoring = {"X": 1, "Y": 2, "Z": 3}

lose = {"A": "Z", "B": "X", "C": "Y"}
win = {"A": "Y", "B": "Z", "C": "X"}
draw = {"A": "X", "B": "Y", "C": "Z"}

lookup = {"X": lose, "Y": draw, "Z": win}


def score_move(op: str, you: str) -> int:
    if (op, you) in win.items():
        return scoring[you] + 6
    elif (op, you) in draw.items():
        return scoring[you] + 3
    elif (op, you) in lose.items():
        return scoring[you]
    raise ValueError(f"Invalid move {op} {you}")


def part1(puzzle_input):
    return sum(score_move(*line.split()) for line in puzzle_input)


def part2(puzzle_input):
    return sum(
        score_move(op, lookup[you][op]) for op, you in map(str.split, puzzle_input)
    )


if __name__ == "__main__":
    puzzle_input = aoc_utils.input_string_list()
    print(part1(puzzle_input))
    print(part2(puzzle_input))
