from collections import Counter

import aoc_utils


def parse_line(line: str) -> tuple[int, ...]:
    return tuple(map(int, line.split()))


def get_lists(lines: list[str]) -> tuple[tuple, tuple]:
    parsed = [parse_line(line) for line in lines]
    left, right = list(zip(*parsed))
    return left, right


def part1(lines: list[str]) -> int:
    left, right = get_lists(lines)
    return sum([abs(al - ar) for al, ar in zip(sorted(left), sorted(right))])


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
