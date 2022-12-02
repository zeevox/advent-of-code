import parse

import aoc_utils

template = "inp w\nmul x 0\nadd x z\nmod x 26\ndiv z {}\nadd x {}\neql x w\neql x 0\nmul y 0\nadd y 25\nmul y x\nadd y {}\nmul z y\nmul y 0\nadd y w\nadd y {}\nmul y x\nadd z y"

segments = aoc_utils.input_string().replace("inp", "\ninp").split("\n\n")

for segment in segments:
    result = parse.parse(template, segment.strip())
    if result is not None:
        result = tuple(result)
        print(result)
    print(result)
    print()
