import argparse
import functools
import hashlib
import heapq
import inspect
import itertools
import operator
import re
import timeit
from pathlib import Path
from typing import Any, Callable, Collection, Generator, Iterable


def _get_filename_interactively() -> str:
    return input("Input filename: ").strip()


def _get_caller() -> str:
    return inspect.stack()[-1].filename


def _get_path_to_file(filename: str) -> Path:
    return Path(_get_caller()).parent.parent / "inputs" / filename


def _get_default_filename() -> str:
    """Makes educated guess based on caller filename on which input we should use."""
    caller: str = _get_caller()
    match = re.search(r"Day(\d+).*\.py", caller)
    if match:
        return f"{match.group(1)}.txt"


def _get_ref_to_file() -> Path:
    # by default, we attempt to get the puzzle input as a function argument
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "filename",
        type=str,
        nargs="?",
        help="The filename of the puzzle input",
        default=None,
    )

    filename = (
        parser.parse_args().filename
        or _get_default_filename()
        or _get_filename_interactively()
    )
    file = _get_path_to_file(filename)

    assert file is not None
    return file


_file: Path | None = None


def input_file() -> Path:
    global _file
    if _file is None:
        _file = _get_ref_to_file()
    return _file


def input_string() -> str:
    """read input into a string"""
    return input_file().read_text().strip()


def input_int_list() -> list[int]:
    """parse input into a list of ints"""
    return list(map(int, input_string_list()))


def input_string_list() -> list[str]:
    """parse input into a list of strings"""
    return list(map(str.rstrip, input_string().splitlines()))


def input_block_list() -> list[str]:
    """input split by paragraph i.e. two newlines"""
    return input_string().split("\n\n")


def filter_empty(li: Iterable) -> list:
    """remove empty entries (e.g. when splitting a string)"""
    return list(filter(None, li))


def flat_map(func: Callable[..., Iterable], iterable: Iterable) -> list:
    """map a function returning a list over a list and concatenate the results"""
    output = []
    for item in iterable:
        output.extend(func(item))
    return output


def gen_flat_map(
    func: Callable[..., Iterable], iterable: Iterable
) -> Generator[Any, None, None]:
    """map a function returning a list over a list and concatenate the results"""
    for item in iterable:
        yield from func(item)


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


def timing(f: Callable, repeat: int = 10):
    @functools.wraps(f)
    def wrap(*args, **kw):
        result = f(*args, **kw)
        time = timeit.timeit(stmt=lambda: f(*args, **kw), number=repeat) / repeat
        print(f"func:{f.__name__!r} took: {time:.2n} sec")
        return result

    return wrap
