import itertools
import queue

from parse import parse

import aoc_utils

"""
I spent way too long faffing around with rotating the
vector so I ended up writing a rather manual and ugly
function to generate this lookup table for me instead
"""
orientations = {
    0: lambda v: (v[0], v[2], -v[1]),
    1: lambda v: (-v[2], v[0], -v[1]),
    2: lambda v: (-v[0], -v[2], -v[1]),
    3: lambda v: (v[2], -v[0], -v[1]),
    4: lambda v: (v[2], -v[1], v[0]),
    5: lambda v: (v[1], v[2], v[0]),
    6: lambda v: (-v[2], v[1], v[0]),
    7: lambda v: (-v[1], -v[2], v[0]),
    8: lambda v: (-v[1], v[0], v[2]),
    9: lambda v: (-v[0], -v[1], v[2]),
    10: lambda v: (v[1], -v[0], v[2]),
    11: lambda v: (v[0], v[1], v[2]),
    12: lambda v: (-v[2], -v[0], v[1]),
    13: lambda v: (v[0], -v[2], v[1]),
    14: lambda v: (v[2], v[0], v[1]),
    15: lambda v: (-v[0], v[2], v[1]),
    16: lambda v: (-v[0], v[1], -v[2]),
    17: lambda v: (-v[1], -v[0], -v[2]),
    18: lambda v: (v[0], -v[1], -v[2]),
    19: lambda v: (v[1], v[0], -v[2]),
    20: lambda v: (v[1], -v[2], -v[0]),
    21: lambda v: (v[2], v[1], -v[0]),
    22: lambda v: (-v[1], v[2], -v[0]),
    23: lambda v: (-v[2], -v[1], -v[0]),
}


def vector_delta(from_pos, to_pos):
    return tuple(j - i for i, j in zip(from_pos, to_pos))


def parse_scanner(data: str):
    """parse a single scanner's input"""
    data = data.strip().splitlines()
    scanner_no = parse("--- scanner {:d} ---", data[0])
    data = [tuple(int(coord) for coord in line.split(",")) for line in data[1:]]
    return int(scanner_no[0]), data


def gen_deltas(vectors: list[tuple[int, int, int]]):
    """
    for every possible pair of position vectors, calculate the vector between the two.
    NB: for points A, B both A --> B and B --> A are generated; n * (n - 1) items returned
    returned in format (delta, (v_start, v_end))
    """
    yield from (
        (vector_delta(triple1, triple2), (triple1, triple2))
        for triple1, triple2 in itertools.permutations(vectors, 2)
        if triple1 != triple2
    )


if __name__ == "__main__":
    data = dict(map(parse_scanner, aoc_utils.input_block_list()))

    q = queue.Queue()
    beacons = set()
    fixed_scanners = {0: 0}
    scanner_locations = {0: (0, 0, 0)}
    q.put(0)

    while not q.empty():
        fixed_scanner_no = q.get()

        fixed_deltas = dict(
            gen_deltas(
                map(
                    orientations[fixed_scanners[fixed_scanner_no]],
                    data[fixed_scanner_no],
                )
            )
        )

        for potential_scanner_no, potential_data in data.items():
            if (
                fixed_scanner_no == potential_scanner_no
                or potential_scanner_no in fixed_scanners
            ):
                continue
            # print(
            #     f"Comparing scanners {fixed_scanner_no} and {potential_scanner_no}..."
            # )
            for orientation, f_rotate in orientations.items():
                transformed_potential_data = list(map(f_rotate, potential_data))
                potential_deltas = dict(gen_deltas(transformed_potential_data))
                common_deltas = fixed_deltas.keys() & potential_deltas.keys()
                # I know they said 12 but 3 points is enough to triangulate
                if len(common_deltas) >= 3:
                    # print(
                    #     f"Found solution for scanner {potential_scanner_no} with orientation {orientation}. Common points: {len(common_deltas)}"
                    # )

                    q.put(potential_scanner_no)
                    # record the orientation of the scanner for beacon
                    # calculation later
                    fixed_scanners[potential_scanner_no] = orientation

                    # any of the pairs will (read: should) give the same result
                    random_delta = common_deltas.pop()
                    # o is the position vector of the current 'fixed' scanner we are operating on
                    # i is the vector from the scanner to the first beacon of the delta pair
                    # j is the vector from the newly discovered scanner to the
                    # same beacon
                    scanner_locations[potential_scanner_no] = tuple(
                        o + i - j
                        for o, i, j in zip(
                            scanner_locations[fixed_scanner_no],
                            fixed_deltas[random_delta][0],
                            potential_deltas[random_delta][0],
                        )
                    )
                    break

    # print(fixed_scanners, scanner_locations)

    beacons = set()

    for scanner, orientation in fixed_scanners.items():
        offset = scanner_locations[scanner]
        for rotated_point in map(orientations[orientation], data[scanner]):
            beacons.add(tuple(o + i for o, i in zip(offset, rotated_point)))

    print(len(beacons))

    def manhattan(vectors):
        vector1, vector2 = vectors
        return sum(abs(c1 - c2) for c1, c2 in zip(vector1, vector2))

    print(max(map(manhattan, itertools.permutations(scanner_locations.values(), 2))))
