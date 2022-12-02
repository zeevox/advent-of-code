import argparse
import heapq
from pathlib import Path
from typing import Collection, Iterable


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
