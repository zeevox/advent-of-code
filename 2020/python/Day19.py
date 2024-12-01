import re
from functools import lru_cache

import aoc_utils

rules, ms = aoc_utils.input_string().split("\n\n")

rs = {}
for rule in rules.split("\n"):
    rule = rule.split(": ")
    rs[rule[0]] = rule[1]


@lru_cache()
def eval(s, part2=False):
    groups = []
    for group in s.split(" | "):
        cgroup = ""
        for rule in group.split(" "):
            # hacky way of saying "if it's actually a letter"
            if len(rs[rule]) == 3 and rs[rule][0] == '"' and rs[rule][2] == '"':
                cgroup += rs[rule][1]
            elif part2 and rule == "8":
                # could be any non-zero number of 42s, basically
                cgroup += "(" + eval(rs["42"]) + ")+"
            elif part2 and rule == "11":
                # could be 42 31 or 42 42 31 31 or 42 42 42 31 31 31 31 etc...
                # most importantly same number of 42s and 31s
                # assume no more than ten of them, just OR each of the options with a for loop
                # because lookbehinds make getting the NUMBER of matches of the
                # previous one difficult
                cgroup += (
                    "("
                    + "|".join(
                        [
                            "("
                            + eval(rs["42"])
                            + "){"
                            + str(n)
                            + "}("
                            + eval(rs["31"])
                            + "){"
                            + str(n)
                            + "}"
                            for n in range(1, 10)
                        ]
                    )
                    + ")"
                )
            else:
                # recurse for each group
                cgroup += eval(rs[rule])
        groups.append(cgroup)
    return "(" + "|".join(groups) + ")"


for i in [False, True]:
    zero_rule = "^" + eval(rs["0"], i) + "$"

    valids = sum(1 for m in ms.split("\n") if re.match(zero_rule, m))
    print(valids)
    eval.cache_clear()
