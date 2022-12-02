import dataclasses
import itertools
from collections import Counter

import parse

import aoc_utils


def parse_line(s: str):
    """Extract numbers from string like on x=-20..26,y=-36..17,z=-47..7"""
    state, x_min, x_max, y_min, y_max, z_min, z_max = parse.parse(
        "{} x={:d}..{:d},y={:d}..{:d},z={:d}..{:d}", s
    )
    return state == "on", x_min, x_max, y_min, y_max, z_min, z_max


def part1(string: list[str]):
    lit = set()
    for switch_on, xl, xu, yl, yu, zl, zu in map(parse_line, string):
        for xi, yi, zi in itertools.product(
            range(max(xl, -50), min(xu, 50) + 1),
            range(max(yl, -50), min(yu, 50) + 1),
            range(max(zl, -50), min(zu, 50) + 1),
        ):
            if switch_on:
                lit.add((xi, yi, zi))
            else:
                lit.discard((xi, yi, zi))
    return len(lit)


@dataclasses.dataclass
class Cuboid:
    x_min: int
    x_max: int
    y_min: int
    y_max: int
    z_min: int
    z_max: int

    def __and__(self, other):
        intersect = Cuboid(
            max(self.x_min, other.x_min),
            min(self.x_max, other.x_max),
            max(self.y_min, other.y_min),
            min(self.y_max, other.y_max),
            max(self.z_min, other.z_min),
            min(self.z_max, other.z_max),
        )
        return (
            None
            if (
                intersect.x_min > intersect.x_max
                or intersect.y_min > intersect.y_max
                or intersect.z_min > intersect.z_max
            )
            else intersect
        )

    def __len__(self):
        """Return volume of the cuboid"""
        return (
            (self.x_max - self.x_min + 1)
            * (self.y_max - self.y_min + 1)
            * (self.z_max - self.z_min + 1)
        )

    def __hash__(self):
        return hash(
            (
                self.x_min,
                self.x_max,
                self.y_min,
                self.y_max,
                self.z_min,
                self.z_max,
            )
        )


def part2(string: list[str]) -> int:
    cuboids = Counter()
    for switch_on, *cuboid in map(parse_line, string):
        cuboid = Cuboid(*cuboid)
        new_cuboids = Counter()
        for other_cuboid, count in cuboids.items():
            intersect = cuboid & other_cuboid
            if intersect is not None:
                new_cuboids[intersect] -= count
        if switch_on:
            # add the cuboid itself
            new_cuboids[cuboid] += 1
        cuboids.update(new_cuboids)

    return sum(map(lambda x: len(x[0]) * x[1], cuboids.items()))


if __name__ == "__main__":
    string = aoc_utils.input_string_list()

    print(part1(string))
    print(part2(string))
