from aoc_utils import input_string, md5sum

puzzle_input: str = input_string()

number: int = 0
while not md5sum(puzzle_input + str(number)).startswith("000000"):
    number += 1
print(number)
