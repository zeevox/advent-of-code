import aoc_utils


def sum_one_to_n(x: int):
    """Formula extracted to helper function for shorter lambda"""
    return (x * (x + 1)) // 2


def main(xs: list[int]):
    """
    Pretty much just brute force it
    For each x-coordinate that the crabs could reduce to,
    Calculate total fuel required to get there for all the crabs
    And take the minimum of the generator expression
    """
    return (
        min(sum(abs(y - i) for y in xs) for i in range(max(xs))),
        min(sum(sum_one_to_n(abs(y - i)) for y in xs) for i in range(max(xs))),
    )


if __name__ == "__main__":
    print(*main(list(map(int, aoc_utils.input_string().split(",")))), sep="\n")
