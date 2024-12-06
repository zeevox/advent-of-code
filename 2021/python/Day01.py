import itertools

import aoc_utils


def main(xs: list[int]) -> int:
    print(sum(x < y for x, y in itertools.pairwise(xs)))

    return sum(
        sum(xs[i - 1 : i + 2]) > sum(xs[i - 2 : i + 1]) for i in range(2, len(xs) - 1)
    )


if __name__ == "__main__":
    print(main(aoc_utils.input_int_list()))
