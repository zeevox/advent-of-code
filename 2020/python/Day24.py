from collections import defaultdict
from copy import deepcopy

import aoc_utils

delta = {
    "nw": (0, 1),
    "ne": (1, 0),
    "e": (1, -1),
    "se": (0, -1),
    "sw": (-1, 0),
    "w": (-1, 1),
}


def parse(s):
    x, y = 0, 0
    i = 0
    while i < len(s):
        if s[i] in ["n", "s"]:
            d = delta[s[i : i + 2]]
            i += 2
        else:
            d = delta[s[i]]
            i += 1
        x += d[0]
        y += d[1]
    return x, y


def parsing_test():
    # should return ref. tile i.e. (0, 0)
    print(parse("nwwswee"))
    # should print (3, -3)
    print(parse("esenee"))


def adjacent_tiles(c):
    for d in delta.values():
        yield (c[0] + d[0], c[1] + d[1])


def count_black_tiles(tiles):
    return sum(flips % 2 == 1 for tile, flips in tiles.items())


def cellular_automata(tiles):
    new_tiles = deepcopy(tiles)

    # abusing the defaultdict functionality
    # initialise all the adjacent tiles that could change value on this round
    for tile in new_tiles:
        for _ in adjacent_tiles(tile):
            pass
    for tile, flips in tiles.items():
        adjacent_black_tiles = sum(
            tiles.get(adj_tile, 0) % 2 == 1 for adj_tile in adjacent_tiles(tile)
        )

        if (
            (flips % 2 == 1
            and (adjacent_black_tiles == 0 or adjacent_black_tiles > 2))
            or (flips % 2 != 1
            and adjacent_black_tiles == 2)
        ):
            new_tiles[tile] += 1
    return new_tiles


if __name__ == "__main__":
    tiles = defaultdict(int)
    for line in aoc_utils.input_string_list():
        tiles[parse(line.strip())] += 1

    print(count_black_tiles(tiles))

    for _ in range(100):
        tiles = cellular_automata(tiles)

    print(count_black_tiles(tiles))
