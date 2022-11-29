#!/usr/bin/python3

import itertools
import aoc_utils
import queue


def get_neighbours(point, size):
    offsets = itertools.product((-1, 0, 1), repeat=len(point))
    for offset in offsets:
        if all(x == 0 for x in offset):
            continue
        coords = tuple(map(sum, zip(point, offset)))
        if all(0 <= coord < size for coord in coords):
            yield coords


def cycle(arr):
    # these are the octopi that we need to process
    to_flash = queue.Queue()
    # each octopus can only flash once per cycle
    flashed = set()
    # iterate over all cells, add 1 and if it's greater
    # than nine, mark it as an octopus to flash
    for y, row in enumerate(arr):
        for x, _ in enumerate(row):
            arr[y][x] += 1
            if arr[y][x] > 9:
                to_flash.put((x, y))
                flashed.add((x, y))
    # keep going as long as new octopi keep having
    # their energy level increased beyond 9
    while not to_flash.empty():
        x, y = to_flash.get()
        for nx, ny in get_neighbours((x, y), len(arr)):
            arr[ny][nx] += 1
            # only let each octopus flash once per cycle
            if arr[ny][nx] > 9 and (nx, ny) not in flashed:
                to_flash.put((nx, ny))
                flashed.add((nx, ny))
    # reset all those octopi that flashed to energy level zero
    # otherwise neighbours will keep increasing their energy level
    for fx, fy in flashed:
        arr[fy][fx] = 0
    # return the total number of flashes that occurred
    # as well as the new grid for the next cycle
    return len(flashed), arr


if __name__ == "__main__":
    grid = list(list(map(int, line)) for line in aoc_utils.input_string_list())
    total = 0
    for _ in range(100):
        flashes, grid = cycle(grid)
        total += flashes
    print(f"{total} flashes after 100 steps")

    grid = list(list(map(int, line)) for line in aoc_utils.input_string_list())
    flashed = 0
    i = 0
    while flashed != 100:
        flashed, grid = cycle(grid)
        i += 1
    print(f"{i} steps to first synchronised flash")
