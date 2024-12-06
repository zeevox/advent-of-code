from collections import defaultdict

import aoc_utils

database = defaultdict(list)
all_ingredients = []
all_allergens = set()

inp = aoc_utils.input_string()
for line in inp.strip().splitlines():
    split = line.strip().split(" (contains ")

    ingredients = set(split[0].strip().split(" "))
    all_ingredients += ingredients

    allergens = set(split[1].strip()[:-1].split(", "))
    all_allergens |= allergens

    for allergen in allergens:
        # print(allergen, ingredients)
        database[allergen] += [set(ingredients)]

for allergen, ingredients in database.items():
    database[allergen] = set.intersection(*ingredients)

hypoallergenic = set(all_ingredients) - set.union(*database.values())

print(
    "Part 1:",
    sum(
        all_ingredients.count(hypoallergenic_ingredient)
        for hypoallergenic_ingredient in hypoallergenic
    ),
)

while any(len(ingredients) != 1 for ingredients in database.values()):
    for allergen, ingredients in database.items():
        if len(ingredients) == 1:
            for other_allergen, value in database.items():
                if allergen is not other_allergen:
                    value -= ingredients
print("Part 2:", ",".join(next(iter(database[k])) for k in sorted(database)))
