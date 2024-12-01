import re

import aoc_utils

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def main(parttwo=False):
    passports = aoc_utils.input_block_list()
    valid = 0
    for passport in passports:
        passport = passport.replace("\n", " ")
        if any(passport.count(field) != 1 for field in fields):
            continue
        # this RegEx is *so* close and yet I'm still getting an off-by-one error somewhere
        # it outputs 138 when it should be 137 but not exactly sure why
        if (
            parttwo
            and re.match(
                r"(?=.*byr:(19[2-9][0-9]|200[1-2]))(?=.*iyr:(201[0-9]|2020))(?=.*eyr:(202[0-9]|2030))(?=.*hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in))(?=.*hcl:#(?:[0-9a-fA-F]{3}){1,2})(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth))(?=.*pid:\d{9})",
                passport,
            )
            is None
        ):
            continue
        if parttwo:
            print(passport)
        valid += 1
    return valid


print(main())
print(main(True))
