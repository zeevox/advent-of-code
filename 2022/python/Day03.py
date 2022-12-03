from string import ascii_lowercase, ascii_uppercase

import more_itertools

from aoc_utils import *

from typing import Iterable


def parse(rucksack: str) -> tuple[str, str]:
    split_point = len(rucksack) // 2
    return rucksack[:split_point], rucksack[split_point:]


def value(letter: str) -> int:
    return (ascii_lowercase + ascii_uppercase).index(letter) + 1


def common(*strings: Iterable[str]) -> set[str]:
    return set.intersection(*map(set, strings))


def part1(rucksacks: list[str]) -> int:
    return sum(
        sum(value(letter) for letter in common(parse(line)))
        for line in rucksacks
    )


def part2(rucksacks: list[str]) -> int:
    return sum(
        value(next(iter(set.intersection(*map(set, elfs)))))
        for elfs in more_itertools.chunked(rucksacks, 3)
    )


if __name__ == "__main__":
    inp = input_string_list()
    print(part1(inp))
    print(part2(inp))
