import hashlib


def md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


door_id = "abbhdwsy"

password = ""
password2 = [""] * 8
i = 0
while len(password) < 8 or len("".join(password2)) < 8:
    hash = md5(door_id + str(i))
    if hash[:5] == "00000":
        if len(password) < 8:
            password += hash[5]
        if hash[5] in "01234567" and password2[int(hash[5])] == "":
            password2[int(hash[5])] = hash[6]

    i += 1

print(password)
print(password2)
