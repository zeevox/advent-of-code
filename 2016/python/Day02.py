#!/usr/bin/python3

with open(f"2016/inputs/02.txt", "r") as f:
    instructions = f.read().splitlines()

start = 5
code = 0
for line in instructions:
    for command in line:
        if command == "U" and start > 3:
            start -= 3
        elif command == "D" and start < 7:
            start += 3
        elif command == "L" and start % 3 != 1:
            start -= 1
        elif command == "R" and start % 3 != 0:
            start += 1
    code = code * 10 + start

print(code)

keypad = [
    [None, None, "1", None, None],
    [None, "2", "3", "4", None],
    ["5", "6", "7", "8", "9"],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None],
]

sx, sy = 0, 2
code = ""
for line in instructions:
    for command in line:
        if command == "U":
            px, py = sx, sy - 1
            if py < 0 or keypad[py][px] is None:
                continue
            sy = py
        elif command == "D":
            px, py = sx, sy + 1
            if py > 4 or keypad[py][px] is None:
                continue
            sy = py
        elif command == "L":
            px, py = sx - 1, sy
            if px < 0 or keypad[py][px] is None:
                continue
            sx = px
        elif command == "R":
            px, py = sx + 1, sy
            if px > 4 or keypad[py][px] is None:
                continue
            sx = px
    code += keypad[sy][sx]

print(code)
