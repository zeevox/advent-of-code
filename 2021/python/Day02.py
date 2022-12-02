#!/usr/bin/python3

import aoc_utils


def part1():
    xs = aoc_utils.input_string_list()
    x, z = 0, 0
    for i in xs:
        c, d = i.split()
        if c == "forward":
            x += int(d)
        elif c == "down":
            z -= int(d)
        elif c == "up":
            z += int(d)
    print(abs(x) * abs(z))


def part2():
    xs = aoc_utils.input_string_list()
    x, z, aim = 0, 0, 0
    for i in xs:
        c, d = i.split()
        if c == "forward":
            x += int(d)
            z -= aim * int(d)
        elif c == "down":
            aim -= int(d)
        elif c == "up":
            aim += int(d)
    print(abs(x) * abs(z))


if __name__ == "__main__":
    part1()
    part2()
