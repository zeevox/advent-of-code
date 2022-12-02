#!/usr/bin/python3

import queue

import networkx as nx

import aoc_utils


def count_double_lowers(path: list[str]):
    count = 0
    for n in path:
        if not n.islower():
            continue
        if path.count(n) >= 2:
            count += 1
    return count


def main(lines: list[str]):
    g = nx.Graph()
    for line in lines:
        start_node, end_node = line.strip().split("-")
        g.add_edge(start_node, end_node)
    q = queue.Queue()
    q.put(["start"])
    paths = []
    while not q.empty():
        node = q.get()
        if node[-1] == "end":
            paths.append(node)
            continue
        for n in g.neighbors(node[-1]):
            if n == "start" or (n.islower() and n in node):
                continue
            q.put(node + [n])
    print(len(paths))

    q = queue.Queue()
    q.put(["start"])
    paths = []
    while not q.empty():
        node = q.get()
        if node[-1] == "end":
            paths.append(node)
            continue
        for n in g.neighbors(node[-1]):
            if n == "start" or (
                n.islower() and count_double_lowers(node) > 0 and n in node
            ):
                continue
            q.put(node + [n])
    print(len(paths))


if __name__ == "__main__":
    main(aoc_utils.input_string_list())
