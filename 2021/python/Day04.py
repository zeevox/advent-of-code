#!/usr/bin/python3

import itertools
import random
import re
import sys
from collections import *
from pprint import pprint
from copy import deepcopy

import operator
import aoc_utils


def main(numbers: list[int], boards: list[list[int]]):
    turns = max(
        zip(
            range(len(boards)),
            map(lambda x: min_drawn_numbers_for_board(numbers, x), boards),
        ),
        key=lambda x: x[1][2],
    )
    # index of board, (index of row, number of turns required)
    board_index, (is_column, row_index, turns_required) = turns
    print(turns)
    print(
        sum(map(sum, filter_minus_ones_from_board(boards[board_index])))
        * numbers[turns_required - 1]
    )


def parse_board(board: str) -> list[int]:
    return list(map(lambda x: list(map(int, x.split())), board.split("\n")))


def filter_minus_ones_from_board(board: list[list[int]]) -> list[list[int]]:
    return list(map(lambda row: list(filter(lambda x: x != -1, row)), board))


def min_drawn_numbers_for_board(
    numbers: list[int], board: list[list[int]]
) -> tuple[bool, int, int]:
    index = 0
    while all(sum(row) > -5 for row in board) and all(
        sum(col) > -5 for col in zip(*board)
    ):
        for row in board:
            if numbers[index] in row:
                row[row.index(numbers[index])] = -1
        index += 1
    if [-1, -1, -1, -1, -1] in board:
        return False, board.index([-1, -1, -1, -1, -1]), index
    for i, column in enumerate(zip(*board)):
        if sum(column) == -5:
            return True, i, index


if __name__ == "__main__":
    numbers_up, *boards_up = aoc_utils.input_block_list()
    numbers = list(map(int, numbers_up.strip().split(",")))
    boards = list(map(parse_board, boards_up))
    main(numbers, boards)
