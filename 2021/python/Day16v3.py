#!/usr/bin/python3

import dataclasses
import math
import operator
import queue
from typing import Optional

import aoc_utils


hex_lookup = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex2bin(s: str):
    return "".join(hex_lookup[c] for c in s)


@dataclasses.dataclass
class Packet:
    version: int
    type: int
    data: str
    value: Optional[int] = None
    extra: Optional[str] = None
    subpackets: Optional[list] = None

    def __init__(self, bin_str: str) -> None:
        self.version = int(bin_str[:3], 2)
        self.type = int(bin_str[3:6], 2)
        self.data = bin_str[6:]

        if self.type == 4:
            value = ""
            for i in range(0, len(self.data), 5):
                value += self.data[i + 1 : i + 5]
                if self.data[i] == "0":
                    break
            self.value = int(value, 2)
            self.extra = self.data[i + 5 :]
            self.data = self.data[: i + 5]
        else:
            self.subpackets = []
            self.length_type = self.data[0]
            self.data = self.data[1:]
            unparsed_data = ""
            if self.length_type == "0":
                bit_count = int(self.data[:15], 2)
                unparsed_data = self.data[15 : 15 + bit_count]
                self.extra = self.data[15 + bit_count :]
                while len(unparsed_data) > 0:
                    subpacket = Packet(unparsed_data)
                    unparsed_data = subpacket.extra
                    self.subpackets.append(subpacket)
            elif self.length_type == "1":
                number_of_subpackets = int(self.data[:11], 2)
                unparsed_data = self.data[11:]
                while len(self.subpackets) < number_of_subpackets:
                    subpacket = Packet(unparsed_data)
                    unparsed_data = subpacket.extra
                    self.subpackets.append(subpacket)
                self.extra = unparsed_data
            self.data = self.data[: ~len(self.extra)]

    def version_sum(self) -> int:
        return self.version + (
            sum(p.version_sum() for p in self.subpackets)
            if self.subpackets is not None
            else 0
        )

    def evaluate(self) -> int:
        if self.type == 0:
            return sum(p.evaluate() for p in self.subpackets)
        elif self.type == 1:
            return math.prod(p.evaluate() for p in self.subpackets)
        elif self.type == 2:
            return min(p.evaluate() for p in self.subpackets)
        elif self.type == 3:
            return max(p.evaluate() for p in self.subpackets)
        elif self.type == 4:
            return self.value
        elif self.type == 5:
            return int(self.subpackets[0].evaluate() > self.subpackets[1].evaluate())
        elif self.type == 6:
            return int(self.subpackets[0].evaluate() < self.subpackets[1].evaluate())
        elif self.type == 7:
            return int(self.subpackets[0].evaluate() == self.subpackets[1].evaluate())


if __name__ == "__main__":
    with aoc_utils.input() as f:
        s = f.read().strip()

    root = Packet(hex2bin(s))
    print(root.version_sum())
    print(root.evaluate())
