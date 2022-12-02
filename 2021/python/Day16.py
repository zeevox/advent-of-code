#!/usr/bin/python3

import dataclasses
import math

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


class Packet:
    version: int
    type: int
    value: int
    extra: str
    subpackets: list["Packet"] = []

    def __init__(self, bin_str: str) -> None:
        self.version = int(bin_str[:3], 2)
        self.type = int(bin_str[3:6], 2)
        data = bin_str[6:]

        if self.type == 4:
            value = ""
            i = 0
            for i in range(0, len(data), 5):
                value += data[i + 1 : i + 5]
                if data[i] == "0":
                    break
            self.value = int(value, 2)
            self.extra = data[i + 5 :]
            data = data[: i + 5]
            return

        # all other packets are operator packets and
        # thus have subpackets contained within them
        self.subpackets = []
        self.length_type = data[0]

        # for easier indexing later on remove 1st char
        data = data[1:]

        # length type 0 provides the number of bits to read
        if self.length_type == "0":
            bit_count = int(data[:15], 2)
            unparsed_data = data[15 : 15 + bit_count]
            self.extra = data[15 + bit_count :]
            while len(unparsed_data) > 0:
                subpacket = Packet(unparsed_data)
                unparsed_data = subpacket.extra
                self.subpackets.append(subpacket)

        # length type 1 provides the number of subpackets to read
        elif self.length_type == "1":
            number_of_subpackets = int(data[:11], 2)
            unparsed_data = data[11:]
            while len(self.subpackets) < number_of_subpackets:
                subpacket = Packet(unparsed_data)
                unparsed_data = subpacket.extra
                self.subpackets.append(subpacket)
            self.extra = unparsed_data

    def version_sum(self) -> int:
        """add up the version numbers in all packets"""
        return self.version + (
            sum(p.version_sum() for p in self.subpackets)
            if self.subpackets is not None
            else 0
        )

    def evaluate(self) -> int:
        """evaluate the expression represented by the BITS transmission"""
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
            return int(
                self.subpackets[0].evaluate() > self.subpackets[1].evaluate()
            )
        elif self.type == 6:
            return int(
                self.subpackets[0].evaluate() < self.subpackets[1].evaluate()
            )
        elif self.type == 7:
            return int(
                self.subpackets[0].evaluate() == self.subpackets[1].evaluate()
            )
        raise ValueError("Cannot evaluate this expression")


if __name__ == "__main__":
    s = aoc_utils.input_string()

    root = Packet(hex2bin(s))
    print(root.version_sum())
    print(root.evaluate())
