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
    print(f"  #{n2s(rs[0][1])}#{n2s(rs[1][1])}#{n2s(rs[2][1])}#{n2s(rs[3][1])}#")
    print("  ########")


rno_pos = range(2, 10, 2)


def valid_room(a, r):
    return r in [(0, 0), (0, a)]


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


@lru_cache()
def move_r2c(c, rs):
    # moves from rooms into corridor
    for rno, (r1, r2) in enumerate(rs):
        # room is empty
        if r1 == 0 and r2 == 0:
            continue
        # room is done
        if r1 == r2 == rno + 1:
            continue
        # room is partially done
        if r1 == 0 and r2 == rno + 1:
            continue

        # otherwise room not done, can move out of it

        # whether we are moving the lower amphipod out
        lower = r1 == 0
        # the amphipod type
        a = r2 if lower else r1
        # the index of the room
        ri = rno_pos[rno]
        # for each position that we can move out into
        for np in move_r2c_valid_pos(ri, c):
            # get the cost of moving there
            moves = abs(ri - np) + (2 if lower else 1)
            cost = moves * (10 ** (a - 1))
            # yield a new game state
            yield (
                cost,
                (
                    replace(c, np, a),
                    replace(rs, rno, (0, 0) if lower else (0, r2)),
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
            cost = abs(ri - apos)
            nc = replace(c, apos, 0)
            if rs[rno][1] == 0:
                cost += 2
                nrs = replace(rs, rno, (0, a))
            else:
                cost += 1
                nrs = replace(rs, rno, (a, rs[rno][1]))
            yield (cost * 10 ** (a - 1), (nc, nrs))


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
        if data[0] == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) and data[1] == (
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
        ):
            return cost
        for add_cost, new_data in move(*data):
            q.put((cost + add_cost, new_data))
            # print("---")
            # print(cost + add_cost)
            # print_diagram(*new_data)
    return 0


def main(diagram: str) -> int:
    c = tuple(s2n(diagram[p]) for p in range(15, 26))
    rs = tuple(tuple(s2n(diagram[p]) for p in r) for r in rps)
    return moves((c, rs))


if __name__ == "__main__":
    print(main(aoc_utils.input_string()))
