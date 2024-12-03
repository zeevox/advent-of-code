import aoc_utils
import re


def part1(lines: list[str]) -> int:
    mul_reg = r"mul\((\d{1,3}),(\d{1,3})\)"
    return sum(int(m1) * int(m2) for d in lines for m1, m2 in re.findall(mul_reg, d))


def part2(lines: list[str]) -> int:
    mul_reg = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"
    enabled = True
    total = 0
    for line in lines:
        for match_str, m1, m2 in re.findall(mul_reg, line):
            if match_str == "do()":
                enabled = True
            elif match_str == "don't()":
                enabled = False

            if enabled and m1 and m2:
                total += int(m1) * int(m2)
    return total


def main():
    data = aoc_utils.input_string_list()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
