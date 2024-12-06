import itertools

import aoc_utils


class Node:
    left = None
    right = None
    parent = None

    def __init__(self, parent, data) -> None:
        self.parent = parent

        if isinstance(data, int):  # leaf node
            self.left = data
            return

        # otherwise data must be two-element tuple
        left, right = data
        self.left, self.right = Node(self, left), Node(self, right)

    @staticmethod
    def from_string(string: str) -> "Node":
        return Node(None, eval(string))

    def depth(self):
        return 1 if self.parent is None else self.parent.depth() + 1

    def is_leaf(self):
        return self.right is None

    def is_pair(self):
        return (not self.is_leaf()) and self.left.is_leaf() and self.right.is_leaf()

    def get_root(self):
        return self if self.parent is None else self.parent.get_root()

    def __str__(self):
        return str(self.left) if self.is_leaf() else f"[{self.left!s}, {self.right!s}]"

    def add_num(self, int_node: "Node"):
        assert self.is_leaf()
        assert self.right is None
        assert int_node.right is None
        self.left += int_node.left

    def __add__(self, other: "Node"):
        temp_node = Node(None, 0)
        temp_node.left = self
        self.parent = temp_node
        temp_node.right = other
        other.parent = temp_node
        return temp_node

    def magnitude(self):
        if self.is_leaf():
            return self.left
        else:
            return 3 * self.left.magnitude() + 2 * self.right.magnitude()


def next_node(node, direction=1):
    stack = [node.get_root()]
    return_next = False
    while stack:
        cur = stack.pop()
        if cur.is_leaf():
            if cur.parent == node:
                return_next = True
            elif return_next:
                # print("!_>", end="")
                return_next = False
                return cur
            # print(cur, end=" ")
        else:
            stack.extend([cur.right, cur.left][::direction])


def next_right(node):
    return next_node(node, 1)


def next_left(node):
    return next_node(node, -1)


def reduce_rule1(root):
    stack = [root]

    while stack:
        node = stack.pop()

        # If any pair is nested inside four pairs, the leftmost such pair
        # explodes
        if node.is_pair() and node.depth() > 4:
            # add to both sides
            adj = next_left(node)
            if adj is not None:
                adj.add_num(node.left)
            adj = next_right(node)
            if adj is not None:
                adj.add_num(node.right)

            # replace pair with a zero
            # convert into intnode
            node.left = 0
            node.right = None

            return False

        if not node.is_leaf():
            stack.extend((node.right, node.left))
    return True


def reduce_rule2(root):
    stack = [root]

    while stack:
        node = stack.pop()

        # If any regular number is 10 or greater, the leftmost such regular
        # number splits.
        if node.is_leaf() and node.left >= 10:
            value = node.left
            node.left = Node(node, value // 2)
            node.right = Node(node, value - value // 2)
            return False

        if not node.is_leaf():
            stack.append(node.right)
            stack.append(node.left)
    return True


def fully_reduce(root):
    done = False
    while not done:
        if reduce_rule1(root):
            done = reduce_rule2(root)
    return None  # remind myself that all is happening in-place


if __name__ == "__main__":
    data = aoc_utils.input_string_list()

    root = Node.from_string(data[0])

    for other in data[1:]:
        root += Node.from_string(other)
        fully_reduce(root)

    # print(root)
    print(root.magnitude())

    magnitudes = []
    for sn1, sn2 in itertools.permutations(data, 2):
        root = Node.from_string(sn1)
        root += Node.from_string(sn2)
        fully_reduce(root)
        magnitudes.append(root.magnitude())

    print(max(magnitudes))
