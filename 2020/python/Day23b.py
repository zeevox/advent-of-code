#!/usr/bin/python3


class cup:
    def __init__(self, label):
        self.label = int(label)

    def link(self, next, previous_by_label):
        self.next, self.previous_by_label = next, previous_by_label


# get the cups, then pad with numbers
def get_cups(s, maxlen):
    yield from map(cup, list(s))
    yield from map(cup, range(len(s) + 1, maxlen + 1))


def process_cups(s, n_cups=1000000):

    # perhaps not the most efficient way of generating a linked list, but it works
    cups = list(get_cups(s, n_cups))
    cups_by_value = sorted(cups, key=lambda x: x.label)

    for i in range(len(cups)):
        this_cup = cups[i]
        next_cup = cups[(i + 1) % len(cups)]
        prev_cup = cups_by_value[this_cup.label - 2]

        this_cup.link(next_cup, prev_cup)
    return cups[0]


def move(current_cup):
    next_three = [
        current_cup.next,
        current_cup.next.next,
        current_cup.next.next.next,
    ]

    destination_cup = current_cup.previous_by_label
    while destination_cup in next_three or current_cup == destination_cup:
        destination_cup = destination_cup.previous_by_label

    current_cup.next = next_three[2].next
    destination_cup.next, next_three[2].next = (
        next_three[0],
        destination_cup.next,
    )

    return current_cup.next


current_cup = process_cups("318946572")
for i in range(10000000):
    current_cup = move(current_cup)

while current_cup.label != 1:
    current_cup = current_cup.next

print(current_cup.next.label * current_cup.next.next.label)
