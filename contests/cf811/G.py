
def solve():
    n = int(input())
    inp = [list(map(int, input().split())) for _ in range(n-1)]
    edges = [(v[0], i+2) for i,v in enumerate(inp)]
    print(edges)

    nodes = {}
    root = next(iter(set(start for start, _ in edges) - set(end for _, end in edges)))
    for start, end in edges:
        nodes.setdefault(start, {})[end] = nodes.setdefault(end, {})

    tree = {root: nodes[root]}
    print(tree)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
