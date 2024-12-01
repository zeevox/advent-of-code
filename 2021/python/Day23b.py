from functools import lru_cache
from queue import PriorityQueue

import aoc_utils

rps = ((31, 45), (33, 47), (35, 49), (37, 51))


def n2s(c):
    """convert the integer to its amphipod meaning"""
    return "." if c == 0 else chr(c + ord("A") - 1)


def s2n(c):
    """convert amphipod representation to integer"""
    return 0 if c == "." else ord(c) - ord("A") + 1


def print_diagram(c, rs):
    """given the tuple for the corridor and rooms print the diagram"""
    print("#############")
    m = tuple(map(n2s, c))
    print(f"#{''.join(m)}#")
    print(f"###{n2s(rs[0][0])}#{n2s(rs[1][0])}#{n2s(rs[2][0])}#{n2s(rs[3][0])}###")
    for i in range(1, len(rs[0])):
        print(f"  #{n2s(rs[0][i])}#{n2s(rs[1][i])}#{n2s(rs[2][i])}#{n2s(rs[3][i])}#")
    print("  #########")


rno_pos = range(2, 10, 2)


def valid_room(a, r):
    return all(m in [0, a] for m in r)


def replace(tup: tuple, index: int, value):
    return tup[:index] + (value,) + tup[index + 1 :]


def move_r2c_valid_pos(ri, c):
    # moving right
    for p in range(ri + 1, len(c)):
        if c[p] != 0:
            break
        if p in rno_pos:
            continue
        yield p
    # moving left
    for p in range(ri - 1, -1, -1):
        if c[p] != 0:
            break
        if p in rno_pos:
            continue
        yield p


def top_amphi(room):
    return next(((i, a) for i, a in enumerate(room) if a), (None, None))


@lru_cache()
def move_r2c(c, rs):
    # moves from rooms into corridor
    for rno, room in enumerate(rs):
        if valid_room(rno + 1, room):
            continue

        topi, topa = top_amphi(room)
        if topi is None or topa is None:
            continue

        # the index of the room
        ri = rno_pos[rno]

        # for each position that we can move out into
        for np in move_r2c_valid_pos(ri, c):
            # get the cost of moving there
            moves = abs(ri - np) + topi + 1
            cost = moves * (10 ** (topa - 1))
            # yield a new game state
            yield (
                cost,
                (
                    replace(c, np, topa),
                    replace(rs, rno, replace(room, topi, 0)),
                ),
            )


@lru_cache()
def move_c2r(c, rs):
    # take the amphipod and its position in the corridor
    for apos, a in enumerate(c):
        # if there is no amphipod there continue
        if a == 0:
            continue
        # get the appropriate room number for that amphipod
        rno = a - 1
        # get the index of where the amphipod's room joins with the corridor
        ri = rno_pos[rno]
        # if the room is not ready to take the amphipod, ignore
        if not valid_room(a, rs[rno]):
            continue
        # if the route is clear
        if (
            apos > ri
            and not any(c[ri + 1 : apos])
            or apos < ri
            and not any(c[apos + 1 : ri])
        ):
            topi, _ = top_amphi(rs[rno])
            if topi is None:
                topi = 3
            else:
                topi -= 1

            moves = abs(ri - apos) + topi + 1
            nc = replace(c, apos, 0)
            nrs = replace(rs, rno, replace(rs[rno], topi, a))
            yield (moves * 10 ** (a - 1), (nc, nrs))


@lru_cache()
def move(c, rs):
    try:
        yield next(move_c2r(c, rs))
    except StopIteration:
        yield from move_r2c(c, rs)


def moves(initial_data) -> int:
    q = PriorityQueue()
    q.put((0, initial_data))
    while not q.empty():
        (cost, data) = q.get()
        if not any(data[0]) and data[1] == (
            (1, 1, 1, 1),
            (2, 2, 2, 2),
            (3, 3, 3, 3),
            (4, 4, 4, 4),
        ):
            return cost
        for add_cost, new_data in move(*data):
            q.put((cost + add_cost, new_data))
    return 0


def main(diagram: str) -> int:
    c = tuple(s2n(diagram[p]) for p in range(15, 26))
    rbs = [[s2n(diagram[p]) for p in r] for r in rps]
    rs = (
        (rbs[0][0], 4, 4, rbs[0][1]),
        (rbs[1][0], 3, 2, rbs[1][1]),
        (rbs[2][0], 2, 1, rbs[2][1]),
        (rbs[3][0], 1, 3, rbs[3][1]),
    )
    return moves((c, rs))


if __name__ == "__main__":
    print(main(aoc_utils.input_string()))
