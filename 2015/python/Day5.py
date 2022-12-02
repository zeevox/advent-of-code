#!/usr/bin/python3

with open("../inputs/5.txt", "r") as file:
    strings = list(map(str.strip, file.readlines()))

vowels = ["a", "e", "i", "o", "u"]
banned = ["ab", "cd", "pq", "xy"]


def is_vowel(char) -> bool:
    return char in vowels


def nice(string: str) -> bool:
    return next(
        (False for ban in banned if ban in string),
        False
        if len(list(filter(is_vowel, string))) < 3
        else any((letter + letter) in string for letter in set(string)),
    )


def windowed(string: str, width: int):
    for pos in range(len(string) - width + 1):
        yield string[:pos], string[pos : pos + width], string[pos + width :]


def rule4(string: str) -> bool:
    return any(
        window in pre or window in post
        for pre, window, post in windowed(string, 2)
    )


def rule5(string: str) -> bool:
    return any(a == b for _, (a, _, b), _ in windowed(string, 3))


def nice2(string: str) -> bool:
    return rule4(string) and rule5(string)


if __name__ == "__main__":
    print(len(list(filter(nice, strings))))
    print(len(list(filter(nice2, strings))))
