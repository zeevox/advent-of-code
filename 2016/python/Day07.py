import re

import aoc_utils
import more_itertools

data = aoc_utils.input_string_list()


def has_abba(s):
    return any(
        window[:2] == window[::-1][:2] and window[2] != window[3]
        for window in more_itertools.windowed(s, 4)
    )


def has_bab(s, a, b):
    return any(
        window[0] == b and window[1] == a and window[2] == b
        for window in more_itertools.windowed(s, 3)
    )


# data = ["abba[mnop]qrst", "abcd[bddb]xyyx", "aaaa[qwer]tyui", "ioxxoj[asdfgh]zxcvbn"]
# data = ["aba[bab]xyz", "xyx[xyx]xyx", "aaa[kek]eke", "zazbz[bzb]cdb"]
count = 0
ssls = set()
for ip in data:
    bad = set(re.findall(r"\[(.*?)\]", ip))
    good = set(re.split("\\[|\\]", ip)) - bad
    if any(has_abba(s) for s in good) and not any(has_abba(s) for s in bad):
        print(ip)
        count += 1

    for s in good:
        for window in more_itertools.windowed(s, 3):
            if window[0] == window[2] and window[0] != window[1]:
                a, b, _ = window
                for bb in bad:
                    if not has_bab(bb, a, b):
                        continue
                    ssls.add(ip)
                    break
print(count)
print(len(ssls))
