def has_double(s):
    return any(s[i] == s[i + 1] for i in range(len(s) - 1))


def has_only_double(s):
    return any(
        s[i] == s[i + 1]
        and (i >= 1 and s[i - 1] != s[i] or i == 0)
        and (i < len(s) - 2 and s[i + 2] != s[i] or i == len(s) - 2)
        for i in range(len(s) - 1)
    )


def no_decreasing(s):
    return all(int(s[i]) <= int(s[i + 1]) for i in range(len(s) - 1))


def main(start: int, end: int):
    print(
        len(
            list(
                filter(
                    lambda x: has_double(x) and no_decreasing(x),
                    map(str, range(start, end + 1)),
                )
            )
        )
    )

    print(
        len(
            list(
                filter(
                    lambda x: has_only_double(x) and no_decreasing(x),
                    map(str, range(start, end + 1)),
                )
            )
        )
    )


main(387638, 919123)
