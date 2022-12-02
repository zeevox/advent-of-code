import aoc_utils

aoc_utils.SAMPLE = False


def sum_reindeer(calories: str) -> int:
    return sum(map(int, calories.splitlines()))


if __name__ == "__main__":
    calories_sums = list(map(sum_reindeer, aoc_utils.input_block_list()))
    print(max(calories_sums))
    print(sum(list(sorted(calories_sums))[-3:]))
