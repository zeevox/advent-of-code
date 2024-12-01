import aoc_utils


def main():
    inp = aoc_utils.input_string_list()
    li = [False] * (2**10)
    for seat in inp:
        seat = (
            seat.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")
        )
        li[int(seat, 2)] = True
    max = 0
    for i in range(1, len(li)):
        if li[i - 1] and li[i + 1] and not li[i]:
            print(f"Missing {i}")
        if li[i] and i > max:
            max = i
    print(f"Max {max}")


print(main())
