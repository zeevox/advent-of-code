from aoc_utils import *

width = 50
height = 6


def main(commands):
    lit: set[tuple[int, int]] = set()
    for command in commands:
        to_add = set()
        to_del = set()
        match command.split(" "):
            case ["rect", AxB]:
                x, y = tuple(map(int, AxB.split("x")))
                to_add.update(gen_rectangle_coords((0, 0), (x - 1, y - 1)))
            case ["rotate", "column", srx, "by", scount]:
                row_x, count = int(srx[2:]), int(scount)
                for x, y in filter(lambda coord: coord[0] == row_x, lit):
                    to_del.add((x, y))
                    to_add.add((x, (y + count) % height))
            case ["rotate", "row", sry, "by", scount]:
                row_y, count = int(sry[2:]), int(scount)
                for x, y in filter(lambda coord: coord[1] == row_y, lit):
                    to_del.add((x, y))
                    to_add.add(((x + count) % width, y))
        lit -= to_del
        lit.update(to_add)
    print(len(lit))
    print_grid_set_dict(
        lit,
        min_x=0,
        min_y=0,
        max_x=width - 1,
        max_y=height - 1,
        sep="",
        empty=" ",
        filled="\u2588",
    )


if __name__ == "__main__":
    main(input_string_list())
