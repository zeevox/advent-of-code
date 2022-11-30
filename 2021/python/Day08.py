#!/usr/bin/python3

from collections import *

import aoc_utils


def main(xs: list[str]):
    count = 0
    for x in xs:
        inp, out = x.split(" | ")
        out = out.split()
        lens = [len(x) for x in out]
        for l in lens:
            if l in {2, 4, 3, 7}:
                count += 1
    print(count)

    count = 0
    for x in xs:
        inp, out = x.split(" | ")
        out = list(map(set, out.split()))
        inp = inp.split()
        seven = next(filter(lambda x: len(x) == 3, inp))
        four = next(filter(lambda x: len(x) == 4, inp))
        eight = next(filter(lambda x: len(x) == 7, inp))
        one = next(filter(lambda x: len(x) == 2, inp))
        nine = next(
            filter(
                lambda x: len(x) == 6 and all(segment in x for segment in four),
                inp,
            )
        )
        three = next(
            filter(
                lambda x: len(x) == 5 and all(segment in x for segment in seven),
                inp,
            )
        )
        zero = next(
            filter(
                lambda x: len(x) == 6
                and all(segment in x for segment in one)
                and x not in [seven, four, eight, one, nine, three],
                inp,
            )
        )
        six = next(
            filter(
                lambda x: len(x) == 6
                and x not in [seven, four, eight, one, nine, three, zero],
                inp,
            )
        )
        five = next(
            filter(
                lambda x: x not in [seven, four, eight, one, nine, three, zero, six]
                and sum((char in nine) for char in x) == 5,
                inp,
            )
        )
        two = next(
            filter(
                lambda x: x
                not in [seven, four, eight, one, nine, three, zero, six, five],
                inp,
            )
        )

        value = ""
        for digit in out:
            if set(digit) == set(zero):
                value += "0"
            elif set(digit) == set(one):
                value += "1"
            elif set(digit) == set(two):
                value += "2"
            elif set(digit) == set(three):
                value += "3"
            elif set(digit) == set(four):
                value += "4"
            elif set(digit) == set(five):
                value += "5"
            elif set(digit) == set(six):
                value += "6"
            elif set(digit) == set(seven):
                value += "7"
            elif set(digit) == set(eight):
                value += "8"
            elif set(digit) == set(nine):
                value += "9"
        count += int(value)

    print(count)


if __name__ == "__main__":
    main(aoc_utils.input_string_list())
