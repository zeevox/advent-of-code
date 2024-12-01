import aoc_utils

ws = [w.split(",") for w in aoc_utils.input_string_list()]

vs = []
for w in ws:
    v = []
    x, y = 0, 0
    for i in w:
        d = i[0]
        n = int(i[1:])
        if d == "R":
            v += [(x := x + 1, y) for _ in range(n)]
        elif d == "L":
            v += [(x := x - 1, y) for _ in range(n)]
        elif d == "U":
            v += [(x, y := y + 1) for _ in range(n)]
        elif d == "D":
            v += [(x, y := y - 1) for _ in range(n)]
    vs.append(v)

print(
    min(
        map(
            lambda x: abs(x[0]) + abs(x[1]),
            intersects := set(vs[0]) & set(vs[1]),
        )
    )
)
print(
    min(
        {
            vs[0].index(intersect) + vs[1].index(intersect) + 2: intersect
            for intersect in intersects
        }.items(),
        key=lambda x: x[0],
    )[0]
)
