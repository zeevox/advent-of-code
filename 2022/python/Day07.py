from functools import lru_cache
from pathlib import Path

from aoc_utils import input_string

filesystem: dict[Path, set[Path] | int] = {}


def parse_groups(groups: list[list[str]]):
    # start in the root folder
    cwd = Path("/")

    # a group is a list representing a command and its lines of output
    for group in groups:
        cmd, *result = group

        # if this is a listing
        if cmd == "ls":
            # then this entry in the filesystem is a collection of pointers to
            # other files
            filesystem[cwd] = set()

            for entry in result:
                size, name = entry.split()

                # add a pointer for both contained files and subdirectories
                filesystem[cwd].add(cwd / name)

                # but if it is a file then we also add a filesystem entry with
                # its size
                if size.isnumeric():
                    filesystem[cwd / name] = int(size)
        else:  # this is the case that we are changing directories
            # we only care about the directory we are changing to
            directory = cmd.split()[1]

            # amend the current working directory appropriately
            cwd = cwd.parent if directory == ".." else cwd / directory

    # it is stored in a global variable too but return for sanity
    return filesystem


@lru_cache
def size_dir(dir: Path):
    global filesystem
    values = filesystem.get(dir, -1)
    if isinstance(values, int):
        return 0 if values == -1 else values
    else:
        return sum(size_dir(subdir) for subdir in values)


if __name__ == "__main__":
    inp = input_string()

    # split based on each new dollar sign indicating a new command
    groups = [group.splitlines() for group in inp[2:].split("\n$ ")]

    # parse to a flat filesystem of pointers and sizes
    parsed = parse_groups(groups)

    # calculate a dictionry with
    directory_sizes = [
        size_dir(directory)
        for directory, value in parsed.items()
        # line below excludes files
        if not isinstance(value, int)
    ]

    print(sum(v for v in directory_sizes if v <= 100_000))

    at_least = size_dir(Path("/")) - 40000000
    print(min(filter(lambda x: x >= at_least, directory_sizes)))
