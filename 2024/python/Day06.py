import dataclasses
from typing import Literal

import aoc_utils
import tqdm


@dataclasses.dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclasses.dataclass(frozen=True)
class Guard(Point):
    dir: Literal[0, 90, 180, 270] = 0

    def location(self) -> Point:
        return Point(self.x, self.y)

    def turn(self) -> "Guard":
        return Guard(self.x, self.y, (self.dir + 90) % 360)

    def step(self) -> "Guard":
        match self.dir:
            case 0:
                return Guard(self.x, self.y - 1, self.dir)
            case 90:
                return Guard(self.x + 1, self.y, self.dir)
            case 180:
                return Guard(self.x, self.y + 1, self.dir)
            case 270:
                return Guard(self.x - 1, self.y, self.dir)
        msg = "Bad direction"
        raise ValueError(msg)


@dataclasses.dataclass
class Map:
    start: Point
    obstructions: set[Point]
    width: int
    height: int
    extra_obstruction: Point | None = None

    def is_obstructed(self, point: Point) -> bool:
        return point in self.obstructions or point == self.extra_obstruction

    def with_obstruction(self, obstruction: Point) -> "Map":
        return Map(self.start, self.obstructions, self.width, self.height, obstruction)


def get_visited(data: Map) -> set[Guard] | None:
    visited: set[Point] = set()

    guard = Guard(data.start.x, data.start.y)
    while guard.x in range(data.width) and guard.y in range(data.height):
        if guard in visited:
            # hit a loop, continue no further
            return None

        visited.add(guard)
        probe = guard.step()
        guard = guard.turn() if data.is_obstructed(probe.location()) else probe

    return visited


def parse_map(data: list[str]) -> Map:
    start_pos: Point = None
    obstructions: set[Point] = set()
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val == "^":
                start_pos = Point(x, y)
            elif val == "#":
                obstructions.add(Point(x, y))
    return Map(start_pos, obstructions, len(data[0]), len(data))


def is_loopy(data: Map) -> bool:
    return get_visited(data) is None


def part2(data: Map, visited: set[Point]) -> int:
    visited.remove(data.start)
    loops = 0
    for point in tqdm.tqdm(visited, leave=False):
        sol = get_visited(data.with_obstruction(point))
        if sol is None:
            loops += 1
    return loops


def main() -> None:
    data = parse_map(aoc_utils.input_string_list())
    visited = {p.location() for p in get_visited(data)}
    print("Part 1:", len(visited))
    print("Part 2:", part2(data, visited))


if __name__ == "__main__":
    main()
