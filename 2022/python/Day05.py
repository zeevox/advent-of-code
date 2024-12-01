from aoc_utils import input_block_list


def parse_crates(crates):
    return dict(
        enumerate(
            [
                [crate for crate in reversed(stack) if crate != " "]
                for stack in zip(*crates.rstrip().splitlines()[:-1])
            ][1:37:4]
        )
    )


def pm(mv):
    _, c, _, s, _, e = mv.split()
    return int(c), int(s) - 1, int(e) - 1


def main(part1: bool = False) -> str:
    crates, movements = input_block_list()
    stacks: dict[int, list[str]] = parse_crates(crates)
    movements_parsed = list(map(pm, movements.split("\n")))
    for count, start, end in movements_parsed:
        stacks[end] += stacks[start][-count:][:: -1 if part1 else 1]
        stacks[start] = stacks[start][:-count]
    return "".join(stacks[i][-1] for i in range(9))


if __name__ == "__main__":
    print(main(part1=True))
    print(main(part1=False))
