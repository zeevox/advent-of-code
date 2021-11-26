#!/usr/bin/python3
import os
from __main__ import __file__

"""
get the day of the python script calling this function
NB: no validation for filename, it is assumed to be DayXX.py
"""


def get_day():
    return os.path.basename(__file__)[3:5]


"""
get a reference straight to the input file
"""


def input():
    return open(filepath(), "r")


"""
get the filepath of the input
"""


def filepath():
    return f"../inputs/{get_day()}.txt"


"""
parse input into a list of ints
"""


def input_int_list():
    return [int(line.rstrip()) for line in open(filepath(), "r")]


"""
parse input into a list of strings
"""


def input_string_list():
    return [line.rstrip() for line in open(filepath(), "r")]


"""
input split by paragraph i.e. two newlines
"""


def input_block_list():
    return open(filepath(), "r").read().split("\n\n")


"""
remove empty entries (e.g. when splitting a string)
"""


def filter_empty(li):
    return list(filter(None, li))
