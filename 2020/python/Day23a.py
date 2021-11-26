#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils


def inp():
    return int(aoc_utils.input().read())


def destination(search, cups):
    while 1:
        if search in cups:
            return cups.index(search)
        search -= 1
        if search < min(cups):
            search = max(cups)


def move(current, cups):
    current_card = cups[current]

    picked = []
    inv = -1 * (len(cups) - current)
    for i in range(1, 4):
        if inv + i >= 0:
            pick = cups.pop(0)
        else:
            pick = cups.pop(inv + i)
        picked.append(pick)

    print("pick up:", *picked)

    dest = destination(current_card - 1, cups)
    print("destination:", cups[dest])

    new_cups = cups[: dest + 1] + picked + cups[dest + 1 :]
    new_current = (current + 1) % len(new_cups)

    if dest < current:
        for _ in range(min(3, len(new_cups) - (current + 1))):
            new_cups.append(new_cups.pop(0))

    return new_current, new_cups


def print_cups(current, cups):
    print("cups:", end=" ")
    for i, c in enumerate(cups):
        print(f"({c})" if i == current else c, end=" ")
    print()


def output(cups):
    print(*cups[cups.index(1) + 1 :], *cups[: cups.index(1)], sep="")


if __name__ == "__main__":
    current = 0
    # cups = list(map(int, list("389125467")))
    cups = list(map(int, list("318946572")))
    print(current, cups)

    for i in range(100):
        print(f"\n-- move {i+1} --")
        print_cups(current, cups)
        current, cups = move(current, cups)

    print("\n-- final --")
    print_cups(current, cups)
    output(cups)
