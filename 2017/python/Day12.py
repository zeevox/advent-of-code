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

    print(len(nx.node_connected_component(g, 0)))
    print(nx.number_connected_components(g))


if __name__ == "__main__":
    main()
