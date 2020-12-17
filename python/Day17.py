#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils

data = []

class Point():
    def __init__(self, x, y, z, w, state):
        self.x, self.y, self.z, self.w, self.state = x, y, z, w, state

def get_neighbours(x, y, z, w):
    # optimised neighbour-finding process
    neighbours = []
    for p in data:
        if abs(p.x-x)<= 1 and abs(p.y-y)<=1 and abs(p.z-z)<= 1 and abs(p.w-w)<= 1 and not (p.x, p.y, p.z, p.w) == (x, y, z, w):
            neighbours.append(p)
    return neighbours
    # this works too, took 15 minutes though
    #coords = [(x + i, y + j, z + k, w + l) for i in [-1, 0, 1] for j in [-1, 0, 1] for k in [-1, 0, 1] for l in [-1, 0, 1] if not (i, j, k, l) == (0, 0, 0, 0)]
    #return [p for p in data if (p.x, p.y, p.z, p.w) in coords]

def value_at(x, y, z, w):
    point = [p for p in data if (p.x, p.y, p.z, p.w) == (x, y, z, w)]
    return point[0].state if len(point) == 1 else False

inp = aoc_utils.input_string_list()
for j, line in enumerate(inp):
    for i, col in enumerate(line):
        if col == "#":
            data.append(Point(i, j, 0, 0, True))

mx, my, mz, mw = (0, len(inp[0])), (0, len(inp)), (0,1), (0,1)

def cycle(mx, my, mz, mw):
    ndata = []
    for x in range(*mx):
        for y in range(*my):
            for z in range(*mz):
                for w in range(*mw):
                    neighbours = get_neighbours(x, y, z, w)
                    val = value_at(x, y, z, w)
                    #print(x, y, z, val, neighbours)
                    if (val == True and (len(neighbours) == 2 or len(neighbours) == 3)) or (val == False and len(neighbours) == 3):
                        ndata.append(Point(x, y, z, w, True))
    return ndata

#print([(p.x, p.y, p.z) for p in data])

for i in range(6):
    mx, my, mz, mw = (mx[0]-1, mx[1]+1), (my[0]-1, my[1]+1), (mz[0]-1, mz[1]+3), (mw[0]-1, mw[1]+3)
    data = cycle(mx, my, mz, mw)
#    print([(p.x, p.y, p.z) for p in data])

print(len(data))
