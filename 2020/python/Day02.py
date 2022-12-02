#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils


def main(parttwo=False):
    count = 0
    for line in aoc_utils.input_string_list():
        line = re.split("-|: | ", line)
        occurs = line[-1].count(line[2])
        if (
            parttwo
            and (line[-1][int(line[0]) - 1] + line[-1][int(line[1]) - 1]).count(
                line[2]
            )
            == 1
        ):
            count += 1
        elif not parttwo and int(line[0]) <= occurs and int(line[1]) >= occurs:
            count += 1
    return count


print(main())
print(main(True))
