from collections.abc import Sequence, Collection, Iterable

import aoc_utils


def get_width[T](matrix: Sequence[Collection[T]]) -> int:
    return len(matrix[0])


def get_height[T](matrix: Collection[Collection[T]]) -> int:
    return len(matrix)


def rotate[T](matrix: Sequence[Sequence[T]]) -> Sequence[Sequence[T]]:
    return list(zip(*matrix))[::-1]


def get_rotations[T](matrix: Sequence[Sequence[T]]) -> Iterable[Sequence[Sequence[T]]]:
    for i in range(4):
        yield matrix
        matrix = rotate(matrix)


def get_diagonals[T](matrix: Sequence[Sequence[T]]) -> Sequence[Sequence[T]]:
    """Get matrix diagonals that go from the bottom-left to the top-right."""
    height: int = get_height(matrix)
    width: int = get_width(matrix)
    return [
        [
            matrix[row - col][col]
            for col in range(max(row - height + 1, 0), min(row + 1, width))
        ]
        for row in range(height + width - 1)
    ]


def count_overlapping(needle: str, haystack: str) -> int:
    return sum(haystack.startswith(needle, i) for i in range(len(haystack)))


def word_search(matrix: list[str]) -> int:
    total = 0
    for matrix in get_rotations(matrix):
        for row in matrix:
            total += count_overlapping("XMAS", "".join(row))
        for line in get_diagonals(matrix):
            total += count_overlapping("XMAS", "".join(line))
    return total


def is_mas_cross(matrix: list[list[str]]) -> bool:
    assert get_width(matrix) == 3 and get_height(matrix) == 3
    diagonals = [
        "".join(matrix[i][i] for i in range(3)),
        "".join(matrix[i][2 - i] for i in range(3)),
    ]
    return all(word in {"MAS", "SAM"} for word in diagonals)


def solve_puzzle(matrix: list[str]) -> int:
    total = 0
    for row in range(1, get_height(matrix) - 1):
        for col in range(1, get_width(matrix) - 1):
            total += is_mas_cross(
                [[matrix[row + j][col + i] for i in [-1, 0, 1]] for j in [-1, 0, 1]]
            )
    return total


def main():
    puzzle_input = aoc_utils.input_string_list()
    print("Part 1:", word_search(puzzle_input))
    print("Part 2:", solve_puzzle(puzzle_input))


if __name__ == "__main__":
    main()
