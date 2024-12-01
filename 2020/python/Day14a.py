import aoc_utils

mask = ""
mem = {}
for line in aoc_utils.input_string_list():
    i, v = line.split(" = ")
    # print(i,v, mem)
    if i == "mask":
        mask = v
    elif i[:3] == "mem":
        v = int(v)
        adr = int(i[4:-1])
        out = "".join(
            bv if bm == "X" else bm
            for bv, bm in zip(list(f"{v:b}".zfill(36)), list(mask))
        )

        # print(f"{mask}\n{v:36b}\t{v}\n{out}")
        mem[adr] = int(out, 2)

print(sum(mem.values()))
