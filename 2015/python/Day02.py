import itertools
import math

from aoc_utils import input_string_list


def parse(box: str) -> tuple[int, int, int]:
    return tuple(map(int, box.split("x")))


puzzle_input = [parse(line) for line in input_string_list()]

paper = 0
ribbon = 0
for box in puzzle_input:
    edge_pairs = list(itertools.combinations(box, 2))
    surface_areas = list(map(math.prod, edge_pairs))
    paper += 2 * sum(surface_areas) + min(surface_areas)
    perimeters = list(map(sum, edge_pairs))
    ribbon += 2 * min(perimeters) + math.prod(box)

print(paper)
print(ribbon)
