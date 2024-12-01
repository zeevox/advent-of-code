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

print("== Initial database ==")
print(*database.items(), sep="\n")

for allergen, ingredients in database.items():
    database[allergen] = set.intersection(*ingredients)

print("== After iteration ==")
print(*database.items(), sep="\n")

hypoallergenic = set(all_ingredients) - set.union(*database.values())

print("== Hypoallergenic ingredients ==")
print(hypoallergenic)
print(
    sum(
        all_ingredients.count(hypoallergenic_ingredient)
        for hypoallergenic_ingredient in hypoallergenic
    )
)

print("== Dangerous ingredient list ==")
while any(len(ingredients) != 1 for ingredients in database.values()):
    for allergen, ingredients in database.items():
        if len(ingredients) == 1:
            for other_allergen, value in database.items():
                if allergen is not other_allergen:
                    value -= ingredients
print(",".join(list(database[k])[0] for k in sorted(database)))
