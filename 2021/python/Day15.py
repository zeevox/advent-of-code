#!/usr/bin/python3

import aoc_utils
import networkx as nx
import math

###
# reuse from day 9


def adjacent(point, size):
    if point[0] < size[0] - 1:
        yield (point[0] + 1, point[1])
    if point[0] > 0:
        yield (point[0] - 1, point[1])
    if point[1] < size[1] - 1:
        yield (point[0], point[1] + 1)
    if point[1] > 0:
        yield (point[0], point[1] - 1)


def print_grid(grid: list[list], points: set[tuple] = None) -> None:
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if points is None or (x, y) in points:
                print(value, end="")
            else:
                print(".", end="")
        print()


# end reuse from day 9
###


def dist_heuristic(n1: tuple[int], n2: tuple[int]) -> int:
    return (n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2


def part1(grid: list[list]):
    g = nx.DiGraph()
    gx = len(grid[0])
    gy = len(grid)

    for y in range(gy):
        for x in range(gx):
            for adj in adjacent((x, y), (gx, gy)):
                g.add_edge(adj, (x, y), weight=grid[y][x])

    # print_grid(grid, nx.dijkstra_path(g, source=(0, 0), target=(gx - 1, gy - 1)))
    print(
        "Part 1:",
        nx.astar_path_length(
            g,
            source=(0, 0),
            target=(gx - 1, gy - 1),
            heuristic=dist_heuristic,
        ),
    )


# as ugly as it gets
# couldn't figure out neater way under time pressure
offsets = {
    (0, 0): 0,
    (0, 1): 1,
    (1, 0): 1,
    (2, 0): 2,
    (0, 2): 2,
    (1, 1): 2,
    (3, 0): 3,
    (0, 3): 3,
    (1, 2): 3,
    (2, 1): 3,
    (0, 4): 4,
    (4, 0): 4,
    (1, 3): 4,
    (3, 1): 4,
    (2, 2): 4,
    (4, 1): 5,
    (1, 4): 5,
    (3, 2): 5,
    (2, 3): 5,
    (4, 2): 6,
    (2, 4): 6,
    (3, 3): 6,
    (4, 3): 7,
    (3, 4): 7,
    (4, 4): 8,
}


def part2(grid: list[list]):
    # just like part 1 but wrapped in a few for statements

    g = nx.DiGraph()
    gx = len(grid[0])
    gy = len(grid)

    for j in range(5):
        for i in range(5):
            offset = offsets[(i, j)]

            for y in range(gy):
                for x in range(gx):
                    point = (x + i * gx, y + j * gy)
                    for adj in adjacent(point, (gx * 5, gy * 5)):
                        g.add_edge(
                            adj, point, weight=((grid[y][x] + offset - 1) % 9 + 1)
                        )

    print(
        "Part 2:",
        nx.astar_path_length(
            g,
            source=(0, 0),
            target=(gx * 5 - 1, gy * 5 - 1),
            heuristic=dist_heuristic,
        ),
    )


if __name__ == "__main__":
    gmap = aoc_utils.input_string_list()
    grid = [list(map(int, row)) for row in gmap]
    part1(grid)
    part2(grid)
