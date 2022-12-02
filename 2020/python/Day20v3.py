import aoc_utils
from pprint import pprint
from math import prod, sqrt


def parse(inp):
    return {
        int(block[5:9]): block.splitlines()[1:]
        for block in inp.strip().split("\n\n")
    }


# rotate 90° clockwise
def rotate(tile):
    return list(zip(*tile[::-1]))


def flip(tile):
    return tile[::-1]


# N -> 0, E -> 1, S -> 2, W -> 3
def get_edge(tile, side):
    if side == 0:
        return "".join(tile[0])
    elif side == 1:
        return "".join(row[-1] for row in tile)
    elif side == 2:
        return "".join(reversed(tile[-1]))
    elif side == 3:
        return "".join(row[0] for row in reversed(tile))
    return None


def edges(tile):
    for side in range(4):
        yield get_edge(tile, side)


def rotations(tile):
    for _ in range(4):
        yield tile
        tile = rotate(tile)


def arrangements(tile):
    yield from rotations(tile)
    yield from rotations(flip(tile))


def adjacent_tile(tile_id, tile, side, tiles):
    edge = get_edge(tile, side)[::-1]
    for other_tile_id in tiles:
        if tile_id is other_tile_id:
            continue
        for arrangement in arrangements(tiles[other_tile_id]):
            if get_edge(arrangement, (side + 2) % 4) == edge:
                return other_tile_id, arrangement
    return False


def adjacent_tiles(tile_id, tile, tiles):
    for side in range(4):
        yield adjacent_tile(tile_id, tile, side, tiles)


def strip_borders(tile):
    return [row[1:-1] for row in tile[1:-1]]


def process_pattern(pattern):
    for x in range(len(pattern[0])):
        for y in range(len(pattern)):
            if pattern[y][x] == "#":
                yield (x, y)


def count_pattern(image, pattern):
    relative_coords = list(process_pattern(pattern))

    for image in arrangements(image):
        pattern_matches = 0
        for x in range(len(image[0]) - len(pattern[0]) + 1):
            for y in range(len(image) - len(pattern) + 1):
                if all(image[y + j][x + i] == "#" for i, j in relative_coords):
                    pattern_matches += 1
        if pattern_matches > 0:
            return pattern_matches
    return False


# set strip to False to see the grid with borders left in
def render(grid, strip=True):
    lines = []
    for row in grid:
        image_row = (
            map("".join, strip_borders(tile) if strip else tile)
            for _, tile in row
        )
        lines.extend(map(("" if strip else " ").join, zip(*image_row)))

        if not strip:
            lines.append("")
    return lines


if __name__ == "__main__":
    tiles = parse(aoc_utils.input().read())

    corners = [
        tile_id
        for tile_id in tiles
        if list(adjacent_tiles(tile_id, tiles[tile_id], tiles)).count(False)
        == 2
    ]
    print(prod(corners))

    # Part 2

    sidelength = int(sqrt(len(tiles)))
    grid = [[None for _ in range(sidelength)] for _ in range(sidelength)]

    for row in range(sidelength):
        if row == 0:
            # fix top-left corner
            for corner in corners:
                adjacent = list(adjacent_tiles(corner, tiles[corner], tiles))
                if (
                    adjacent[0] == False
                    and adjacent[1]
                    and adjacent[2]
                    and adjacent[3] == False
                ):
                    grid[0][0] = (corner, tiles[corner])
                    break
        else:
            # fix the left-most element in this row
            grid[row][0] = adjacent_tile(*grid[row - 1][0], 2, tiles)

        for col in range(1, sidelength):
            grid[row][col] = adjacent_tile(*grid[row][col - 1], 1, tiles)
    pattern = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]

    rendered = render(grid)
    pattern_count = count_pattern(rendered, pattern)

    pattern_hash_count = "".join(pattern).count("#")
    total_hash_count = "".join(rendered).count("#")
    print(total_hash_count - pattern_count * pattern_hash_count)
