"""Construct and verify potential 21- and 30-branch graphs for degree 57."""
from itertools import combinations


def construct(t):
    q = 29
    assert 3 <= t <= 30
    # Include the vertical direction first, then slopes 0,...,t-2.
    directions = [(0, 1)] + [(1, slope) for slope in range(t - 1)]
    branches = []
    neighbors = {}
    for i, (dx, dy) in enumerate(directions):
        leaves = [(side, a * dx % q, a * dy % q)
                  for side in ("point", "line") for a in range(1, q)]
        parent = ("parent", i)
        neighbors[parent] = set(leaves)
        for leaf in leaves:
            neighbors[leaf] = {parent}
        branches.append(leaves)
    # A line with direction vector y consists of the points x with det(x,y)=1.
    points = [v for v in neighbors if v[0] == "point"]
    lines = [v for v in neighbors if v[0] == "line"]
    for p in points:
        for line in lines:
            if (p[1]*line[2] - p[2]*line[1]) % q == 1:
                neighbors[p].add(line)
                neighbors[line].add(p)
    return neighbors, branches


def verify(t):
    graph, branches = construct(t)
    assert len(graph) == 57*t
    branch_sets = list(map(set, branches))
    for i, leaves in enumerate(branches):
        assert len(leaves) == 56 and graph["parent", i] == branch_sets[i]
        for v in leaves:
            assert len(graph[v]) == t
            for j, other in enumerate(branch_sets):
                assert len(graph[v] & other) == int(i != j)
    # Check every pair for triangles and squares using bit-set neighborhoods.
    ids = {v: i for i, v in enumerate(graph)}
    masks = {v: sum(1 << ids[w] for w in adj) for v, adj in graph.items()}
    for u,v in combinations(graph, 2):
        limit = 0 if v in graph[u] else 1
        assert (masks[u] & masks[v]).bit_count() <= limit
    # Directions appear in order vertical, horizontal, ..., slope 14.
    cycle = [("parent", 1), ("point", 1, 0), ("line", 0, 1),
             ("point", 1, 14), ("line", 2, 0)]
    assert all(cycle[(i+1) % 5] in graph[v] for i,v in enumerate(cycle))
    weight = {v: {"point": 1, "line": -1, "parent": 0}[v[0]] for v in graph}
    assert sum(weight.values()) == 0
    assert all(sum(weight[w] for w in adj) == -(t-1)*weight[v]
               for v,adj in graph.items())
    print(f"{t} branches, {len(graph)} vertices, {sum(map(len,graph.values()))//2} edges,"
          f" girth 5, signed-vector eigenvalue {1-t}")


if __name__ == "__main__":
    verify(21)
    verify(30)
