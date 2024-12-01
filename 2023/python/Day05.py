import dataclasses

import aoc_utils


@dataclasses.dataclass
class Almanac:
    name: str
    mappings: list[tuple[range, int]]

    def __init__(self, definition: str) -> None:
        header, *lines = definition.splitlines()
        self.name = header.split()[0]
        mappings = []
        for line in lines:
            dest_range_start, source_range_start, range_length = map(int, line.split())
            mappings.append(
                (
                    range(source_range_start, source_range_start + range_length),
                    dest_range_start - source_range_start,
                )
            )
        self.mappings = mappings

    def map(self, source: int) -> int:
        for mapping, offset in self.mappings:
            if source not in mapping:
                continue
            return source + offset
        return source


def parse_seeds(seeds_str: str) -> list[int]:
    return list(map(int, seeds_str.split(": ")[1].split()))


def main():
    seeds_str, *maps = aoc_utils.input_block_list()
    seeds = parse_seeds(seeds_str)
    almanacs = [Almanac(definition) for definition in maps]
    for almanac in almanacs:
        seeds = map(almanac.map, seeds)
    seeds = list(seeds)
    print("Part 1:", min(seeds))


if __name__ == "__main__":
    main()
