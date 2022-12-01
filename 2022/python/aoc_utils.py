#!/usr/bin/python3

import argparse
from pathlib import Path

def input_file() -> Path:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help="The filename of the puzzle input")
    args = parser.parse_args()
    return Path(__file__).parent.parent / "inputs" / args.filename


def input_string():
    """read input into a string"""
    return input_file().read_text().strip()


def input_int_list():
    """parse input into a list of ints"""
    return list(map(int, input_string_list()))


def input_string_list():
    """parse input into a list of strings"""
    return list(map(str.rstrip, input_string().splitlines()))


def input_block_list():
    """input split by paragraph i.e. two newlines"""
    return input_string().split("\n\n")


def filter_empty(li):
    """remove empty entries (e.g. when splitting a string)"""
    return list(filter(None, li))
