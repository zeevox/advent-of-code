#!/usr/bin/python3

from operator import itemgetter


def losb(number: int) -> int:
    """lowest odd square integer below number"""
    sqrt = int(number ** 0.5)
    if sqrt % 2 == 0:
        sqrt -= 1
    return sqrt


def part1(number: int) -> int:
    # sqrt of number in bottom-right corner
    br_corner = losb(number)
    # coordinates of this number
    coords = [br_corner // 2, br_corner // 2 * -1]
    # how many extra squares from bottom-right corner
    diff = number - br_corner ** 2
    # which edge the data is located on
    edge = diff // (br_corner + 1)
    # how many extra squares from nearest corner
    diff %= br_corner + 1
    if edge == 0:  # right edge
        coords[0] += 1
        coords[1] += diff - 1
    if edge == 1:  # top edge
        coords[0] -= diff - 1
        coords[1] *= -1
        coords[1] += 1
    if edge == 2:  # left edge
        coords[0] *= -1
        coords[0] -= 1
        coords[1] *= -1
        coords[1] -= diff - 1
    if edge == 3:  # bottom edge
        coords[0] *= -1
        coords[0] += diff - 1
        coords[1] -= 1
    return sum(map(abs, coords))


if __name__ == "__main__":
    print(part1(289326))
