#!/usr/bin/python3

from collections import *
import itertools
import random
import re
import sys
import aoc_utils

"""
https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Case_of_two_moduli
algorithm from https://medium.com/@astartekraus/the-chinese-remainder-theorem-ea110f48248c#04ae
"""
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * modinv(p, n_i) * p
    return sum % prod

"""
https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
"""
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

"""
https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Modular_inverse
"""
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

#############
"""
PART ONE-LINER
"""
ts, buses = int((inp := aoc_utils.input_string_list())[0]), list(map(int, filter(lambda x: x != "x", inp[1].split(","))))
print((b := min(buses, key=lambda x: ((ts // x) + 1) * x)) * ((((ts // b) + 1) * b) - ts))

#############
"""
PART TWO
"""

"""
we are solving a set of modular arithmetic equations. using the sample from the
question, with buses 7, 13, 59, 31, 19 and x representing the timestamp that we
are looking for, 7 divides x, 13 divides x+1, 59 divides x+4, 31 divides x+6...

we can write these as such (using triple equals):
x = 0 mod 7
x = -1 mod 13
x = -4 mod 59
x = -6 mod 31
x = -7 mod 19

however the algorithm would not accept negative numbers
but since this is modular arithmetic we must remember that we can express
x = -1 mod 13
instead as
x = 12 mod 13
and solve those equations instead
"""

buses = aoc_utils.input_string_list()[1]
n = []
a = []
for i, bus in enumerate(buses.split(",")):
    if bus == "x": continue
    n.append(bus:=int(bus))
    a.append(bus-i)
print(chinese_remainder(n,a))


