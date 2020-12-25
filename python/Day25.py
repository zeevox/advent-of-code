#!/usr/bin/python3

import aoc_utils

def calc_loop(subject, end):
    value = 1
    loop_size = 0
    while True:
        value = (value * subject) % 20201227
        loop_size += 1
        if value == end:
            return loop_size


def transform(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * subject) % 20201227
    return value

inp = aoc_utils.input().readlines()
#inp = ["5764801", "17807724"]

card_pk, door_pk = list(map(int, inp))

card_ls = calc_loop(7, card_pk)

encr_key = transform(door_pk, card_ls)

print(encr_key)
