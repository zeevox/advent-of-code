#!/usr/bin/python3

with open("2016/inputs/01.txt", "r") as f:
    instructions = f.read().split(", ")

x = y = rot = 0
visited = {(0, 0)}

for op, *count in instructions:
    count = int("".join(count))

    if op == "L":
        rot = (rot + 270) % 360

    elif op == "R":
        rot = (rot + 90) % 360
    if rot == 0:
        visits = {(x, y + (i + 1)) for i in range(count)}
        if visited & visits:
            print(visited & visits)
        visited |= visits
        y += count
    elif rot == 180:
        visits = {(x, y - (i + 1)) for i in range(count)}
        if visited & visits:
            print(visited & visits)
        visited |= visits
        y -= count
    elif rot == 270:
        visits = {(x - (i + 1), y) for i in range(count)}
        if visited & visits:
            print(visited & visits)
        visited |= visits
        x -= count

    elif rot == 90:
        visits = {(x + (i + 1), y) for i in range(count)}
        if visited & visits:
            print(visited & visits)
        visited |= visits
        x += count
print(abs(x) + abs(y))
