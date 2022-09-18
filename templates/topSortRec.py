from collections import defaultdict


def rec(curr, visited, stack):
    visited[curr] = True
    for j in graph[curr]:
        if not visited[j]:
            rec(j, visited, stack)
    stack.append(curr)
    return


def topsort(g, n):
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            rec(i, visited, stack)
    return stack[::-1]


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
