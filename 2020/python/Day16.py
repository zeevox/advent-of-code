# !/usr/bin/python3

import re

import aoc_utils

inp = aoc_utils.input_string_list()
rules = {(x := re.split(r": |-| or ", s))[0]: list(map(int, x[1:])) for s in inp[:20]}
# print(rules)


def valid_any(n):
    return any(valid(n, rule) for rule in rules.values())


def valid(n, rule):
    return (n >= rule[0] and n <= rule[1]) or (n >= rule[2] and n <= rule[3])


sum = 0
ts = inp[inp.index("nearby tickets:") + 1 :]
for ticket in inp[inp.index("nearby tickets:") + 1 :]:
    for value in map(int, ticket.split(",")):
        if not valid_any(value):
            #            print(value)
            sum += value
            ts.remove(ticket)

print(sum)

ts = [list(map(int, ticket.split(","))) for ticket in ts]

cols = {}
myticket = list(map(int, inp[inp.index("your ticket:") + 1].split(",")))
for n, rule in rules.items():
    # if n[:9] != "departure":
    #    continue
    for col in range(len(ts[0])):
        if all(valid(int(t[col]), rule) for t in ts):
            cols[n] = [*cols.get(n, []), col]

# print(cols)

fixed = []
while len(fixed) != len(cols):
    for col in cols.values():
        if len(col) == 1:
            if col[0] not in fixed:
                fixed.append(col[0])
        else:
            for f in fixed:
                if f in col:
                    col.remove(f)
    # print(cols, fixed)
# print(cols)

p = 1
for k, v in cols.items():
    if k[:9] == "departure":
        p *= myticket[v[0]]

print(p)
