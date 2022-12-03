from string import ascii_letters

import more_itertools

from aoc_utils import *

from typing import Iterable


def parse(rucksack: str) -> tuple[str, str]:
    split_point = len(rucksack) // 2
    return rucksack[:split_point], rucksack[split_point:]


def value(letter: str) -> int:
    assert len(letter) == 1
    return ascii_letters.index(letter) + 1


def common(strings: Iterable[str]) -> set[str]:
    return set.intersection(*map(set, strings))


value_line = lambda line: common(parse(line))


def part1(rucksacks: list[str]) -> int:
    return sum(map(value, flat_map(value_line, rucksacks)))


def part2(rucksacks: list[str]) -> int:
    return sum(
        value(next(iter(set.intersection(*map(set, elfs)))))
        for elfs in more_itertools.chunked(rucksacks, 3)
    )


if __name__ == "__main__":
    inp = input_string_list()
    print(part1(inp))
    print(part2(inp))
