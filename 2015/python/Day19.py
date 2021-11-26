#!/usr/bin/python3

import re
from pprint import pprint

with open("2015/inputs/19.txt", "r", encoding="utf-8") as f:
    data = f.read().strip()

# use the empty line before the input molecule to split the data
replacements_str, input_molecule = data.split("\n\n")

# now split the replacements into a list of lines
replacements = replacements_str.split("\n")

# use pprint to make sense of the data
pprint(replacements)

# could use a set instead of a list
possible_replaced_molecules = []

# iterate over every given replacement
for replacement in replacements:
    initial, final = replacement.split(" => ")
    # split the string in every possible place
    # check whether the second part begins with the initial molecule(s)
    for i in range(len(input_molecule)):
        # could invert the if statement instead
        if input_molecule[i:].startswith(initial):
            # combine the first half, replacement, the rest of the molecule
            replaced_molecule = (
                input_molecule[:i]
                + final
                + input_molecule[i:].removeprefix(initial)
            )
            # set-like logic to avoid duplicates
            if replaced_molecule not in possible_replaced_molecules:
                possible_replaced_molecules.append(replaced_molecule)

# this is the answer for part 1
print(len(possible_replaced_molecules))


def all_indices(string, substring):
    """find all locations in a string where substring is located"""
    indices = []
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index == -1:
            break
        indices.append(index)
        index += 1
    return indices


def all_indices_regex(string, substring):
    """find all locations in a string where substring is located,
    overlapping permitted, using simple regex approach"""
    return [match.start() for match in re.finditer(f"(?={substring})", string)]


# Day 2 doesn't actually always work, it depends on the randomness of the order
# of items coming out from the set into the min function. So if it doesn't
# work, try running it again and again and again until it works. Because it
# will, I know it will. I've tested it.

iterations = 0
while input_molecule != "e":
    iterations += 1
    possible_shorter_molecules = set()
    for replacement in replacements:
        initial, final = replacement.split(" => ")
        for i in all_indices(input_molecule, final):
            possible_shorter_molecules.add(
                input_molecule[:i]
                + initial
                + input_molecule[i:].removeprefix(final)
            )
    input_molecule = min(possible_shorter_molecules, key=len)

# this is the answer for part 2
print(iterations)

# So here is an incredibly hacky solution for Part 2 that will always work
# (assuming the input is valid).
number_of_uppercase_letters = 0
for character in input_molecule:
    if character.isupper():
        number_of_uppercase_letters += 1
print(
    number_of_uppercase_letters
    - input_molecule.count("Rn")
    - input_molecule.count("Ar")
    - 2 * input_molecule.count("Y")
    - 1
)
