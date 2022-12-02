#!/usr/bin/python3

import parse

import aoc_utils


def triangle(n: int):
    return n * (n + 1) // 2


def gen_x_coords(v_x: int):
    max_x = triangle(v_x)
    yield from (max_x - triangle(n) for n in range(v_x, -1, -1))


def gen_initial_vx(x_max: int):
    for v_x in range(x_max + 1):
        for x in gen_x_coords(v_x):
            if x_min <= x <= x_max:
                yield v_x
            if x >= x_min:
                break


if __name__ == "__main__":
    data = aoc_utils.input_string()
    result = parse.parse("target area: x={:d}..{:d}, y={:d}..{:d}", data)
    if not isinstance(result, parse.Result):
        raise ValueError("Invalid input data")

    x_min, x_max, y_min, y_max = result

    print("Part 1:", triangle(y_min))

    total = 0
    for v_iy in range(y_min, -y_min):
        for v_ix in gen_initial_vx(x_max):
            x, y = 0, 0
            v_x, v_y = v_ix, v_iy
            while x <= x_max and y >= y_min:
                x, y = x + v_x, y + v_y
                if y_min <= y <= y_max and x_min <= x <= x_max:
                    total += 1
                    break
                v_y -= 1
                if v_x > 0:
                    v_x -= 1
    print("Part 2:", total)
