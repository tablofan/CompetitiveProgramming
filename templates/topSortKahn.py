from collections import defaultdict, deque
def topsort(graph, nodes)


def main():
    nodes = 0
    mapping = defaultdict(int)
    for _ in range(int(input())):
        a, b = input().split()  # a is a prereq of b
        if a not in mapping:
            mapping[a] = nodes
            nodes += 1
        if b not in mapping:
            mapping[b] = nodes
            nodes += 1
        graph[mapping[a]].append(mapping[b])
    mapping = {v:k for k,v in mapping.items()}
    print([mapping[i] for i in topsort(graph, nodes)])


if __name__ == "__main__":
    graph = defaultdict(list)
    main()