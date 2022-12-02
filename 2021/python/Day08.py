#!/usr/bin/python3


from typing import Callable, Iterable

import aoc_utils


def first_with(predicate: Callable, iterable: Iterable) -> str:
    return next(filter(predicate, iterable))


def main(xs: list[str]):
    print(
        sum(
            sum(len(x) in {2, 3, 4, 7} for x in x.split(" | ")[1].split())
            for x in xs
        )
    )

    count = 0
    for x in xs:
        inp, out = x.split(" | ")
        out = list(map(set, out.split()))
        inp = inp.split()

        seven = first_with(lambda x: len(x) == 3, inp)
        four = first_with(lambda x: len(x) == 4, inp)
        eight = first_with(lambda x: len(x) == 7, inp)
        one = first_with(lambda x: len(x) == 2, inp)
        nine = first_with(
            lambda x: len(x) == 6 and all(segment in x for segment in four),
            inp,
        )
        three = first_with(
            lambda x: len(x) == 5 and all(segment in x for segment in seven),
            inp,
        )
        zero = first_with(
            lambda x: len(x) == 6
            and all(segment in x for segment in one)
            and x not in [seven, four, eight, one, nine, three],
            inp,
        )
        six = first_with(
            lambda x: len(x) == 6
            and x not in [seven, four, eight, one, nine, three, zero],
            inp,
        )
        five = first_with(
            lambda x: x not in [seven, four, eight, one, nine, three, zero, six]
            and sum((char in nine) for char in x) == 5,
            inp,
        )
        two = first_with(
            lambda x: x
            not in [seven, four, eight, one, nine, three, zero, six, five],
            inp,
        )
        mapping: list[tuple[str, ...]] = list(
            map(
                lambda x: tuple(sorted(list(x))),
                [
                    zero,
                    one,
                    two,
                    three,
                    four,
                    five,
                    six,
                    seven,
                    eight,
                    nine,
                ],
            )
        )

        value = "".join(
            str(mapping.index(tuple(sorted(list(digit))))) for digit in out
        )
        count += int(value)

    print(count)


if __name__ == "__main__":
    main(aoc_utils.input_string_list())
