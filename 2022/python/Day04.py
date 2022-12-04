from aoc_utils import *


def pe(e):
    a, b = e.split("-")
    return int(a), int(b)


def ce(e1, e2):
    e1a, e1b = e1
    e2a, e2b = e2
    return e1a >= e2a and e1b <= e2b


def ove(e1, e2):
    e1a, e1b = e1
    e2a, e2b = e2
    return e1b >= e2a and e1a <= e2a or e2b >= e1a and e2a <= e1a


def parse(line):
    e1, e2 = list(map(pe, line.split(",")))
    return ce(e1, e2) or ce(e2, e1)


def parse2(line):
    e1, e2 = list(map(pe, line.split(",")))
    return ove(e1, e2) or ove(e2, e1)


def main(inp):
    return sum(parse(line) for line in inp)


def main2(inp):
    return sum(parse2(line) for line in inp)


if __name__ == "__main__":
    inp = input_string_list()
    print(main(inp))
    print(main2(inp))
