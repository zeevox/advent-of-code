from aoc_utils import *

door_id: str = input_string()

password = ""
password2 = [""] * 8
i = 0
while len(password) < 8 or len("".join(password2)) < 8:
    hsh = md5sum(door_id + str(i))
    if hsh[:5] == "00000":
        if len(password) < 8:
            password += hsh[5]
        if hsh[5] in "01234567" and password2[int(hsh[5])] == "":
            password2[int(hsh[5])] = hsh[6]

    i += 1

print(password)
print("".join(password2))
