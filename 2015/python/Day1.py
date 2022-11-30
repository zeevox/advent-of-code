#!/usr/bin/python3

with open("../inputs/1.txt", "r") as inp_file:
    puzzle_input = inp_file.read()


def maina():
    floor = 0
    for bracket in puzzle_input:
        if bracket == "(":
            floor += 1
        if bracket == ")":
            floor -= 1
    return floor


def mainb():
    floor = 0
    for index, bracket in enumerate(puzzle_input):
        if floor < 0:
            return index
        if bracket == "(":
            floor += 1
        if bracket == ")":
            floor -= 1


if __name__ == "__main__":
    print(maina())
    print(mainb())
