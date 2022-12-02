#!/usr/bin/python3

import operator

import aoc_utils


def common_count(xs: list[str], index: int):
    col = list(map(operator.itemgetter(index), xs))
    if col.count("1") > col.count("0"):
        return "1", "0"
    return ("X", "X") if col.count("1") == col.count("0") else ("0", "1")


def main(xs: list[str]):
    gamma = ""
    epsilon = ""
    for index in range(len(xs[0])):
        commons = common_count(xs, index)
        gamma += commons[0]
        epsilon += commons[1]

    print(int(gamma, 2) * int(epsilon, 2))

    xs1 = list(xs)
    i = 0
    while len(xs1) > 1:
        char = common_count(xs1, i)[0]
        if char == "X":
            char = "1"
        xs1 = list(filter(lambda x: x[i] == char, xs1))
        i += 1

    xs2 = list(xs)
    i = 0
    while len(xs2) > 1:
        char = common_count(xs2, i)[1]
        if char == "X":
            char = "0"
        xs2 = list(filter(lambda x: x[i] == char, xs2))
        i += 1

    print(int(xs1[0], 2) * int(xs2[0], 2))


if __name__ == "__main__":
    main(aoc_utils.input_string_list())
