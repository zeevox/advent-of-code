import more_itertools

from aoc_utils import *


def parse(rs: str):
    return rs[: len(rs) // 2], rs[len(rs) // 2 :]


from string import ascii_lowercase, ascii_uppercase


def main(inp):
    sump = 0
    for line in inp:
        f, s = parse(line)
        sf, ss = set(f), set(s)
        common = sf.intersection(ss)
        for letter in common:
            if letter in ascii_lowercase:
                sump += ascii_lowercase.index(letter) + 1
            elif letter in ascii_uppercase:
                sump += ascii_uppercase.index(letter) + 27
    print(sump)


def mainp(inp):
    sump = 0
    for a, b, c in more_itertools.chunked(inp, 3):
        common = set(a).intersection(set(b)).intersection(set(c))
        for letter in common:
            if letter in ascii_lowercase:
                sump += ascii_lowercase.index(letter) + 1
            elif letter in ascii_uppercase:
                sump += ascii_uppercase.index(letter) + 27
    print(sump)


if __name__ == "__main__":
    inp = input_string_list()
    main(inp)
    mainp(inp)
