import aoc_utils


def main(coords, instructions):
    coords = {tuple(map(int, coord.split(","))) for coord in coords.splitlines()}
    folds = [(s[11], int(s[13:])) for s in instructions.splitlines()]

    printed = False
    # dir is one of x or y
    # number is the coordinate line along which to fold
    for dir, num in folds:
        to_remove = set()
        new_coords = set()
        for px, py in coords:
            if dir == "x" and px > num:
                to_remove.add((px, py))
                new_coords.add((num - abs(px - num), py))
            elif dir == "y" and py > num:
                to_remove.add((px, py))
                new_coords.add((px, num - abs(py - num)))
        coords -= to_remove
        coords |= new_coords
        if not printed:
            print(f"Part 1: {len(coords)} points after first fold")
            printed = True

    print("#### Part 2: Decipher the 8 characters below")
    for y in range(max(c[1] for c in coords) + 1):
        for x in range(max(c[0] for c in coords) + 1):
            if (x, y) in coords:
                print("#", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    main(*aoc_utils.input_block_list())
