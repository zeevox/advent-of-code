import itertools

import aoc_utils


def validate(report: list[int]) -> bool:
    # all increasing or all decreasing
    # consecutive entries differ by 1, 2, or 3
    diffs = [a - b for a, b in itertools.pairwise(report)]
    return all(d in {1, 2, 3} for d in diffs) or all(d in {-1, -2, -3} for d in diffs)


def validate2(report: list[int]) -> bool:
    if validate(report):
        return True
    return any(validate(report[:i] + report[i + 1 :]) for i in range(len(report)))


def part1(reports: list[str]):
    return sum(validate([int(e) for e in r.split()]) for r in reports)


def part2(reports: list[str]):
    return sum(validate2([int(e) for e in r.split()]) for r in reports)


if __name__ == "__main__":
    print(part1(aoc_utils.input_string_list()))
    print(part2(aoc_utils.input_string_list()))
