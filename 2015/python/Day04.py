import hashlib


def md5(string: str) -> str:
    return hashlib.md5(string.encode("utf-8")).hexdigest()


puzzle_input: str = "yzbqklnj"

number: int = 0
while not md5(puzzle_input + str(number)).startswith("000000"):
    number += 1
print(number)
