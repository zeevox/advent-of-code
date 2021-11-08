#!/usr/bin/python3

import networkx as nx
import functools
import operator

def parse_line(line: str) -> list[tuple[int, int]]:
    node, children = line.strip().split(" <-> ")
    children = children.split(",")
    return [(int(node), int(child)) for child in children]


def main():
    with open("2017/inputs/12.txt", "r") as f:
        lines = list(map(parse_line, f.readlines()))

    g = nx.Graph()
    g.add_edges_from(functools.reduce(operator.iconcat, lines, []))

    connected_nodes = set()
    for edge in nx.edge_bfs(g, 0):
        connected_nodes.update(edge)

    print(len(connected_nodes))
    print(len(list(nx.connected_components(g))))

if __name__ == "__main__":
    main()
