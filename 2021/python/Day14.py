from collections import Counter, defaultdict

import aoc_utils
import more_itertools


def main(molecule: str, replacements):
    """my initial, naïve attempt at solving this"""

    rules = {}
    for rule in replacements.strip().splitlines():
        init, end = rule.split(" -> ")
        rules[init] = end

    print(molecule)
    for _ in range(10):
        insertions = []
        for i in range(len(molecule) - 1):
            pair = molecule[i : i + 2]
            if pair in rules:
                insertions.append((i + 1, rules[pair]))
        for ii, ic in reversed(insertions):
            molecule = molecule[:ii] + ic + molecule[ii:]
        print(molecule)

    c = Counter(molecule).most_common()
    print(c[0][1] - c[-1][1])


def main2(molecule: str, replacements: str, iterations: int = 10):
    rules = {}
    for rule in replacements.strip().splitlines():
        init, end = rule.split(" -> ")
        rules[init] = end

    # similarly to one of the earlier days, have a
    # dictionary that stores the number of each type
    # of pair instead of a list of all the pairs themselves
    # sheer luck that my puzzle input had no overlapping pairs e.g. HH
    # because my initial parsing did not account for that
    pairs = defaultdict(int)
    for pair in map("".join, more_itertools.windowed(molecule, 2)):
        pairs[pair] += 1

    # we do not care about the iteration step we are
    # on, discard the counter variable
    for _ in range(iterations):
        # we call list() to prevent an error, since we are
        # updating the list that we are iterating over
        for pair, count in list(pairs.items()):
            # inverted if statement for less indentation
            # but also turns out all pairs are in rules
            # so kinda useless if statement anyway
            if pair not in rules:
                continue

            # we cannot reset to zero here, as this pair may have been
            # or will be affected by other substitutions in this iteration
            pairs[pair] -= count

            # add appropriately to the two new element-pairs formed
            pairs[pair[0] + rules[pair]] += count
            pairs[rules[pair] + pair[1]] += count

    # admittedly Counter is somewhat ott here, could have used
    # defaultdict or any other of the myriad of solutions
    c = Counter()
    for elements, count in pairs.items():
        for element in elements:
            c[element] += count

    # adjust for first and last elements which are never changed
    # these are not double counted so we add one to double count them
    c[molecule[0]] += 1
    c[molecule[-1]] += 1

    cmc = c.most_common()
    print(cmc[0][1] // 2 - cmc[-1][1] // 2)


if __name__ == "__main__":
    a, b = aoc_utils.input_block_list()
    main2(a, b, 10)
    main2(a, b, 40)
