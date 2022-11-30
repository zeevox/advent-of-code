#!/usr/bin/python3

with open("../inputs/5.txt", "r") as file:
    strings = list(map(str.strip, file.readlines()))

vowels = ["a", "e", "i", "o", "u"]
banned = ["ab", "cd", "pq", "xy"]


def is_vowel(char) -> bool:
    return char in vowels


def nice(string: str) -> bool:
    for ban in banned:
        if ban in string:
            return False

    if len(list(filter(is_vowel, string))) < 3:
        return False

    for letter in set(string):
        if (letter + letter) in string:
            return True
    return False


def windowed(string: str, width: int):
    for pos in range(len(string) - width + 1):
        yield string[:pos], string[pos : pos + width], string[pos + width :]


def rule4(string: str) -> bool:
    for pre, window, post in windowed(string, 2):
        if window in pre or window in post:
            return True
    return False


def rule5(string: str) -> bool:
    for _, (a, _, b), _ in windowed(string, 3):
        if a == b:
            return True
    return False


def nice2(string: str) -> bool:
    return rule4(string) and rule5(string)


if __name__ == "__main__":
    print(len(list(filter(nice, strings))))
    print(len(list(filter(nice2, strings))))
