#!/usr/bin/python3

from pprint import pprint

with open("2015/inputs/19.txt", "r", encoding="utf-8") as f:
    data = f.read().strip()

replacements_str, input_molecule = data.split("\n\n")

replacements = replacements_str.split("\n")

pprint(replacements)

possible_replaced_molecules = []

for replacement in replacements:
    to_replace, replaced = replacement.split(" => ")
    for i in range(len(input_molecule)):
        if input_molecule[i:].startswith(to_replace):
            replaced_molecule = (
                input_molecule[:i]
                + replaced
                + input_molecule[i:].removeprefix(to_replace)
            )
            if replaced_molecule not in possible_replaced_molecules:
                possible_replaced_molecules.append(replaced_molecule)

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


iterations = 0
while input_molecule != "e":
    iterations += 1
    possible_shorter_molecules = set()
    for replacement in replacements:
        to_replace, replaced = replacement.split(" => ")
        for i in all_indices(input_molecule, replaced):
            possible_shorter_molecules.add(
                input_molecule[:i]
                + to_replace
                + input_molecule[i:].removeprefix(replaced)
            )
    input_molecule = min(possible_shorter_molecules, key=len)
print(iterations)
