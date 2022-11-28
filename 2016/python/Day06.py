#!/usr/bin/python3


from collections import Counter

with open(f"2016/inputs/06.txt", "r") as f:
    data = f.readlines()


for col in zip(*data):
    print(Counter(col).most_common(1)[0][0], end="")


for col in zip(*data):
    print(Counter(col).most_common()[-1][0], end="")
