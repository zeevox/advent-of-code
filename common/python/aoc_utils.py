import argparse
import operator
import itertools
import hashlib
import heapq
from pathlib import Path
from typing import Any, Collection, Iterable


def input_file() -> Path:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename", type=str, help="The filename of the puzzle input"
    )
    args = parser.parse_args()
    return Path(__file__).parent.parent / "inputs" / args.filename


def input_string(file: Path = input_file()) -> str:
    """read input into a string"""
    return file.read_text().strip()


def input_int_list(file: Path = input_file()) -> list[int]:
    """parse input into a list of ints"""
    return list(map(int, input_string_list(file)))


def input_string_list(file: Path = input_file()) -> list[str]:
    """parse input into a list of strings"""
    return list(map(str.rstrip, input_string(file).splitlines()))


def input_block_list(file: Path = input_file()) -> list[str]:
    """input split by paragraph i.e. two newlines"""
    return input_string(file).split("\n\n")


def filter_empty(li: Iterable) -> list:
    """remove empty entries (e.g. when splitting a string)"""
    return list(filter(None, li))


def nlargest(n: int, li: Collection, key=None) -> list:
    """get the n largest items in a list in descending order"""
    if n < 1:
        return []
    if n == 1:
        return [max(li, key=key)]
    if n > len(li) // 4:
        return list(sorted(li, key=key, reverse=True)[:3])
    return heapq.nlargest(n, li, key=key)


def nsmallest(n: int, li: Collection, key=None) -> list:
    """get the `n` smallest items in a list in ascending order"""
    if n < 1:
        return []
    if n == 1:
        return [min(li, key=key)]
    if n > len(li) // 4:
        return list(sorted(li, key=key)[:n])
    return heapq.nsmallest(n, li, key=key)


def md5sum(string: str) -> str:
    return hashlib.md5(string.encode("utf-8")).hexdigest()


def gen_rectangle_coords(corner1: tuple[int, int], corner2: tuple[int, int]):
    """Yield all coordinates enclosed by a rectangle with corners corner1 and corner2"""
    yield from itertools.product(
        range(corner1[0], corner2[0] + 1), range(corner1[1], corner2[1] + 1)
    )


def print_grid_set_dict(
    grid: dict[tuple[int, int], Any] | set[tuple[int, int]],
    min_x: int | None = None,
    max_x: int | None = None,
    min_y: int | None = None,
    max_y: int | None = None,
    sep: str = "",
    filled: str = "#",
    empty: str = ".",
) -> None:
    coords = grid.keys() if isinstance(grid, dict) else grid
    if min_x is None:
        min_x = min(coords, key=operator.itemgetter(0))[0]
    if max_x is None:
        max_x = max(coords, key=operator.itemgetter(0))[0]
    if min_y is None:
        min_y = min(coords, key=operator.itemgetter(1))[1]
    if max_y is None:
        max_y = max(coords, key=operator.itemgetter(1))[1]
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) not in coords:
                print(empty, end=sep)
                continue
            print(grid[(x, y)] if isinstance(grid, dict) else filled, end=sep)
        print()
