import itertools
from collections import Counter, defaultdict
from functools import lru_cache, partial, reduce

import more_itertools
from sortedcontainers import SortedDict, SortedList, SortedSet

from aoc_utils import *

from pathlib import Path

from dataclasses import dataclass


class File:
    name: str
    size: int

    def __init__(self, string: str):
        size, filename = string.split()
        self.size = int(size)
        self.name = filename.strip()


class Directory:
    name: str
    subdirectories = dict()
    files = dict()

    def __init__(self, name: str):
        self.name = name

    def size(self):
        return sum(file.size for file in self.files.values()) + sum(
            dir.size() for dir in self.subdirectories.values()
        )


from pprint import pprint

filesystem: dict[Path, set[Path] | int] = {}


def parse_groups(groups: list[list[str]]):
    cwd = Path("/")
    for group in groups:
        cmd, *result = group
        if cmd == "ls":
            filesystem[cwd] = set()
            for entry in result:
                size, name = entry.split()
                filesystem[cwd].add(cwd / name)
                if size.isnumeric():
                    filesystem[cwd / name] = int(size)
        else:
            print(cmd)
            directory = cmd.split()[1]
            cwd = cwd.parent if directory == ".." else cwd / directory
    return filesystem


@lru_cache()
def size_dir(dir: Path):
    global filesystem
    values = filesystem.get(dir, -1)
    if isinstance(values, int):
        return 0 if values == -1 else values
    else:
        return sum(size_dir(subdir) for subdir in values)


if __name__ == "__main__":
    inp = input_string()
    groups = [group.splitlines() for group in inp[2:].split("\n$ ")]
    parsed = parse_groups(groups)
    directory_sizes = {
        str(directory): size_dir(directory)
        for directory, value in parsed.items()
        if not isinstance(value, int)
    }
    print(directory_sizes)
    s = 0
    for k, v in directory_sizes.items():
        if v <= 100_000:
            print(k, v)
            s += v
    print(s)

    at_least = size_dir(Path("/")) - 40000000
    mins = min(
        sorted(filter(lambda x: x >= at_least, directory_sizes.values()))
    )
    print(mins)
