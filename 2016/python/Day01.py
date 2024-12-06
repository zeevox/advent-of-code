from aoc_utils import input_string

instructions = input_string().split(", ")

x = y = rot = 0
visited = {(0, 0)}
visited_twice = None

for op, *count in instructions:
    count = int("".join(count))

    if op == "L":
        rot = (rot + 270) % 360

    elif op == "R":
        rot = (rot + 90) % 360
    if rot == 0:
        visits = {(x, y + (i + 1)) for i in range(count)}
        if not visited_twice and (place := visited & visits):
            assert len(place) == 1
            visited_twice = next(iter(place))
        visited |= visits
        y += count
    elif rot == 180:
        visits = {(x, y - (i + 1)) for i in range(count)}
        visited |= visits
        y -= count
    elif rot == 270:
        visits = {(x - (i + 1), y) for i in range(count)}
        visited |= visits
        x -= count

    elif rot == 90:
        visits = {(x + (i + 1), y) for i in range(count)}
        visited |= visits
        x += count
print("Part 1:", abs(x) + abs(y))

v2x, v2y = visited_twice
print("Part 2:", abs(v2x) + abs(v2y))
