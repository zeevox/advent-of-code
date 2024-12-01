import queue
from functools import reduce

import aoc_utils


def adjacent(point, size):
    if point[0] < size[0] - 1:
        yield (point[0] + 1, point[1])
    if point[0] > 0:
        yield (point[0] - 1, point[1])
    if point[1] < size[1] - 1:
        yield (point[0], point[1] + 1)
    if point[1] > 0:
        yield (point[0], point[1] - 1)


def print_grid(grid: list[list], points: set[tuple] | None = None) -> None:
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if points is None or (x, y) in points:
                print(value, end="")
            else:
                print(".", end="")
        print()


def main(grid: list[list[int]]):
    critical_levels_sum = 0
    minimum_positions = set()

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if all(
                value < grid[adj[1]][adj[0]]
                for adj in adjacent((x, y), (len(row), len(grid)))
            ):
                minimum_positions.add((x, y))
                critical_levels_sum += value + 1
    print(critical_levels_sum)

    basin_sizes = []

    for minimum in minimum_positions:
        q = queue.Queue()
        q.put(minimum)
        visited = set()
        while not q.empty():
            x, y = q.get()
            if all(
                grid[adj[1]][adj[0]] >= grid[y][x]  # the weak inequality is critical!
                for adj in adjacent((x, y), (len(grid[0]), len(grid)))
                if adj not in visited and adj != (x, y) and grid[adj[1]][adj[0]] != 9
            ):
                for adj in adjacent((x, y), (len(grid[0]), len(grid))):
                    if (
                        adj not in visited
                        and adj != (x, y)
                        and grid[adj[1]][adj[0]] != 9
                    ):
                        q.put(adj)
                visited.add((x, y))

        # print_grid(grid, processed)
        basin_sizes.append(len(visited))
    print(reduce(lambda x, y: x * y, list(sorted(basin_sizes))[-3:], 1))


if __name__ == "__main__":
    main([list(map(int, line)) for line in aoc_utils.input_string_list()])
