#!/usr/bin/python3

import aoc_utils
from string import ascii_lowercase

inputs = list(ascii_lowercase)

register_names = ["w", "x", "y", "z"]


def replace_tuple(tup: tuple, index: int, val) -> tuple:
    return tup[:index] + (val,) + tup[index + 1 :]


def set_register(
    registers: tuple[str, str, str, str], register: str, value: str
) -> tuple[str, str, str, str]:
    return replace_tuple(registers, register_names.index(register), value)


def get_register(registers, register) -> str:
    return registers[register_names.index(register)]


def process(
    command: str, registers: tuple[str, str, str, str]
) -> tuple[str, str, str, str]:
    if command.startswith("inp"):
        _, var = command.split()
        return set_register(registers, var, inputs.pop(0))
    op, var1, var2 = command.split()
    val1 = get_register(registers, var1)
    val2 = get_register(registers, var2) if var2 in register_names else var2
    match [op, var1, val1, val2]:
        case ["add", _, _, "0"]:
            return registers
        case ["add", a, "0", bv]:
            return set_register(registers, a, bv)
        case ["add", a, av, bv]:
            return set_register(registers, a, f"({av}) + ({bv})")
        case ["mul", a, _, "0"]:
            return set_register(registers, a, "0")
        case ["mul", a, _, "1"]:
            return registers
        case ["mul", a, av, bv]:
            return set_register(registers, a, f"({av}) * ({bv})")
        case ["div", _, _, "1"]:
            return registers
        case ["div", a, av, bv]:
            return set_register(registers, a, f"({av}) // ({bv})")
        case ["mod", a, av, bv]:
            if av == bv or av == "0" or bv == "1":
                return set_register(registers, a, "0")
            return set_register(registers, a, f"({av}) % ({bv})")
        case ["eql", a, av, bv]:
            return set_register(
                registers, a, f"1 if (({av}) == ({bv})) else ({av})"
            )
    raise Exception("Unmatched case for", op, var1, val1, val2)


if __name__ == "__main__":
    commands = aoc_utils.input_string_list()
    registers: tuple[str, str, str, str] = ("0", "0", "0", "0")
    from tqdm import tqdm

    for command in tqdm(commands):
        registers = process(command, registers)
        # input(f"{command} -> {registers}")
    print(len(registers[-1]))
    # print(registers[-1])
