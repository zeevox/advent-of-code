from collections import Counter

import aoc_utils

data = aoc_utils.input_string_list()

for col in zip(*data):
    print(Counter(col).most_common(1)[0][0], end="")

for col in zip(*data):
    print(Counter(col).most_common()[-1][0], end="")
