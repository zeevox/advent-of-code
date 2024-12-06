from collections import Counter
from collections.abc import Iterable

import aoc_utils


def get_lists(lines: list[str]) -> tuple[Iterable[int], Iterable[int]]:
    parsed = (line.split() for line in lines)
    left, right = zip(*parsed)
    return map(int, left), map(int, right)


@aoc_utils.timing
def part1(lines: list[str]) -> int:
    left, right = get_lists(lines)
    return sum(abs(al - ar) for al, ar in zip(sorted(left), sorted(right)))


@aoc_utils.timing
def part2(lines: list[str]) -> int:
    left, right = get_lists(lines)
    lookup = Counter(right)
    return sum(al * lookup[al] for al in left)


def main():
    lines = aoc_utils.input_string_list()
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
