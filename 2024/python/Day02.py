import aoc_utils


def validate(report: list[int]) -> bool:
    # all increasing or all decreasing
    # consecutive entries differ by 1, 2, or 3
    diffs = [report[i] - report[i - 1] for i in range(1, len(report))]
    return all(d in {1, 2, 3} for d in diffs) or all(d in {-1, -2, -3} for d in diffs)


def validate2(report: list[int]) -> bool:
    if validate(report):
        return True
    for i in range(0, len(report)):
        if validate(report[:i] + report[i + 1 :]):
            return True
    return False


def part1(reports: list[str]):
    return sum(validate([int(e) for e in r.split()]) for r in reports)


def part2(reports: list[str]):
    return sum(validate2([int(e) for e in r.split()]) for r in reports)


if __name__ == "__main__":
    print(part1(aoc_utils.input_string_list()))
    print(part2(aoc_utils.input_string_list()))
