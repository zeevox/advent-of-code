import more_itertools
from aoc_utils import input_string


def main(buffer, n: int = 4):
    for i, ls in enumerate(more_itertools.windowed(buffer, n)):
        if len(set(ls)) == n:
            return i + n


if __name__ == "__main__":
    inp = input_string()
    print(main(inp, 4))
    print(main(inp, 14))
