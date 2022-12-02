#!/usr/bin/python3
import functools

import parse

import aoc_utils

outcomes = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@functools.cache
def main(a_pos, b_pos, a_score=0, b_score=0):
    if a_score >= 21:
        return 1, 0
    elif b_score >= 21:
        return 0, 1

    a_wins = 0
    b_wins = 0

    for rolled, count in outcomes.items():
        new_a_pos = (a_pos + rolled) % 10
        new_a_score = a_score + new_a_pos + 1

        b_subwins, a_subwins = main(b_pos, new_a_pos, b_score, new_a_score)

        a_wins += a_subwins * count
        b_wins += b_subwins * count

    return a_wins, b_wins


if __name__ == "__main__":
    string = aoc_utils.input_string()
    result = parse.parse(
        "Player 1 starting position: {:d}\nPlayer 2 starting position: {:d}",
        string,
    )
    if not isinstance(result, parse.Result):
        raise ValueError("Invalid input data")
    a, b = result
    print(max(main(a - 1, b - 1)))
