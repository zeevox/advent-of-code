import aoc_utils
import collections
from typing import Literal
from functools import cmp_to_key


def solve(rules: list[tuple[int, int]], manuals: list[list[int]]):
    # map from page to all pages before it
    rules_dict: dict[int, set[int]] = collections.defaultdict(set)
    for page_before, page_after in rules:
        rules_dict[page_after].add(page_before)

    def comparator(page1: int, page2: int) -> Literal[-1, 0, 1]:
        """comparator for page numbers"""
        if page2 in rules_dict[page1]:
            return 1
        elif page1 in rules_dict[page2]:
            return -1
        else:
            return 0

    def is_update_valid(update: list[int]) -> bool:
        """whether the pages of an update are in the right order"""
        for idx, page in enumerate(update[:-1]):
            # if any of the following pages in the update *must*
            # come before the current page, it's invalid
            if any(
                following_page in rules_dict[page]
                for following_page in update[idx + 1 :]
            ):
                return False

        # if we never broke out the loop it's a valid update
        return True

    valid_page_sum: int = 0
    invalid_page_sum: int = 0
    for update in manuals:
        if is_update_valid(update):
            valid_page_sum += update[len(update) // 2]
        else:
            correct_order = sorted(update, key=cmp_to_key(comparator))
            invalid_page_sum += correct_order[len(update) // 2]

    return valid_page_sum, invalid_page_sum


if __name__ == "__main__":
    (rules, manuals) = aoc_utils.input_block_list()
    rules = [(tuple(map(int, rule.split("|")))) for rule in rules.splitlines()]
    assert all(len(rule) == 2 for rule in rules)

    manuals = [list(map(int, line.split(","))) for line in manuals.splitlines()]
    assert all(len(manual) > 0 for manual in manuals)

    solve, part2 = solve(rules, manuals)
    print("Part 1:", solve)
    print("Part 2:", part2)
