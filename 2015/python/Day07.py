from functools import lru_cache

from aoc_utils import input_string_list

instructions = input_string_list()


wires = {out: command for *command, _, out in map(str.split, instructions)}


@lru_cache()
def process(wire: str) -> int:
    if wire.isnumeric():
        return int(wire)

    match wires[wire]:
        case [obj]:
            return process(obj)
        case [var1, "AND", var2]:
            return process(var1) & process(var2)
        case [var1, "OR", var2]:
            return process(var1) | process(var2)
        case [var1, "LSHIFT", var2]:
            return process(var1) << process(var2)
        case [var1, "RSHIFT", var2]:
            return process(var1) >> process(var2)
        case ["NOT", var]:
            return ~process(var)
    raise ValueError(f"uncaught case for {wire}")


if __name__ == "__main__":
    print(process("a"))
    wires["b"] = ["16076"]
    process.cache_clear()
    print(process("a"))
