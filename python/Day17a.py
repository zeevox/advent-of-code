#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils

data = []

class Point():
    def __init__(self, x, y, z, state):
        self.x, self.y, self.z, self.state = x, y, z, state

def get_neighbours(x, y, z):
    coords = [(x + i, y + j, z + k) for i in [-1, 0, 1] for j in [-1, 0, 1] for k in [-1, 0, 1] if not (i, j, k) == (0, 0, 0)]
    return [p for p in data if (p.x, p.y, p.z) in coords]

def value_at(x, y, z):
    point = [p for p in data if (p.x, p.y, p.z) == (x, y, z)]
    return point[0].state if len(point) == 1 else False

inp = aoc_utils.input_string_list()
for j, line in enumerate(inp):
    for i, col in enumerate(line):
        if col == "#":
            data.append(Point(i, j, 0, True))

mx, my, mz = (0, len(inp[0])), (0, len(inp)), (0,1)

def cycle(mx, my, mz):
    ndata = []
    for x in range(*mx):
        for y in range(*my):
            for z in range(*mz):
                neighbours = get_neighbours(x, y, z)
                val = value_at(x, y, z)
                #print(x, y, z, val, neighbours)
                if (val == True and (len(neighbours) == 2 or len(neighbours) == 3)) or (val == False and len(neighbours) == 3):
                    ndata.append(Point(x, y, z, True))
    return ndata

#print([(p.x, p.y, p.z) for p in data])

for i in range(6):
    mx, my, mz = (mx[0]-1, mx[1]+1), (my[0]-1, my[1]+1), (mz[0]-1, mz[1]+3)
    data = cycle(mx, my, mz)
#    print([(p.x, p.y, p.z) for p in data])

print(len(data))
