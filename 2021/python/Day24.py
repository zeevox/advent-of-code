#!/usr/bin/python3

import itertools
import operator
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache, partial, reduce
from typing import Callable

import parse
from sortedcontainers import SortedDict, SortedList, SortedSet

import aoc_utils


@dataclass(unsafe_hash=True)
class State:
    w: int = 0
    x: int = 0
    y: int = 0
    z: int = 0

    def get(self, var_name: str) -> int:
        val = getattr(self, var_name, None)
        return int(var_name) if val is None else val

    def set(self, var_name: str, value: int) -> None:
        return self.__setattr__(var_name, value)


@dataclass
class Operation:
    op: str
    a: "Operation" | str
    b: "Operation" | str

    op_map: dict[str, str] = {
        "add": "+=",
        "mul": "*=",
        "div": "//=",
        "mod": "%=",
    }

    def __str__(self) -> str:
        match [self.op, self.b]:
            case ["add", "0"]:
                return str(self.a)
            case ["mul", "0"]:
                return "0"
            case ["mul", "1"]:
                return str(self.a)
            case ["div", "1"]:
                return str(self.a)
            case _:
                return f"{self.a} {self.op_map[self.op]} {self.b}"


@lru_cache
def process(
    inp: str, minput: tuple[int, ...], state: State
) -> tuple[tuple[int, ...], State]:
    match inp.split():
        case ["inp", var]:
            state.set(var, minput[0])
            minput = minput[1:]
        case [op, var1, var2]:
            state.set(var1, op_map[op](state.get(var1), state.get(var2)))
    return (minput, state)


def processes(inps: list[str], minput: tuple[int, ...]) -> State:
    state = State(0, 0, 0, 0)
    for inp in inps:
        minput, state = process(inp, minput, state)
    return state


from string import ascii_lowercase


def main1(inps: list[str]) -> string:
    state = processes(inps, tuple(map(int, tuple(ascii_lowercase[:14]))))


if __name__ == "__main__":
    print(main1(aoc_utils.input_string_list()))
