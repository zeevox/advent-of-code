import aoc_utils
import collections
from typing import Literal
from functools import cmp_to_key


def solve(rules: list[tuple[int, int]], manuals: list[list[int]]):
    # map from page to all pages before it
    rules_dict: dict[int, set[int]] = collections.defaultdict(set)
    for page_before, page_after in rules:
        rules_dict[page_after].add(page_before)

    middle_page_sum: int = 0
    invalid_updates: list[list[int]] = []
    for uidx, update in enumerate(manuals):
        for idx, page in enumerate(update[:-1]):
            # if any of the following pages in the update *must*
            # come before the current page, it's invalid
            if any(
                following_page in rules_dict[page]
                for following_page in update[idx + 1 :]
            ):
                invalid_updates.append(update)
                break  # don't process any further

        else:  # else of for loop means we didn't break, valid update
            middle_page_sum += update[len(update) // 2]

    def comparator(page1: int, page2: int) -> Literal[-1, 0, 1]:
        if page2 in rules_dict[page1]:
            return 1
        elif page1 in rules_dict[page2]:
            return -1
        else:
            return 0

    invalids_middle_page_sum = sum(
        sorted(update, key=cmp_to_key(comparator))[len(update) // 2]
        for update in invalid_updates
    )

    return middle_page_sum, invalids_middle_page_sum


if __name__ == "__main__":
    (rules, manuals) = aoc_utils.input_block_list()
    rules = [(tuple(map(int, rule.split("|")))) for rule in rules.splitlines()]
    assert all(len(rule) == 2 for rule in rules)

    manuals = [list(map(int, line.split(","))) for line in manuals.splitlines()]
    assert all(len(manual) > 0 for manual in manuals)

    solve, part2 = solve(rules, manuals)
    print("Part 1:", solve)
    print("Part 2:", part2)
