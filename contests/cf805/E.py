def dfs(graph, s, v):
    stack = [s]
    c = 0
    v[s] = True
    while stack:
        curr = stack.pop()
        c += 1
        for neigh in graph[curr]:
            if not v[neigh]:
                stack.append(neigh)
                v[neigh] = True
    return c, v


def solve():
    n = int(input())
    d = [[int(x) for x in input().split()] for _ in range(n)]
    graph = [[] for _ in range(n + 1)]
    f = False
    for i in range(n):
        a, b = d[i]
        if a == b:
            f = True
            break
        graph[a].append(b)
        graph[b].append(a)
    visited = [False for _ in range(n + 1)]
    for i in range(n + 1):
        if len(graph[i]) > 2:
            f = True
            break
        elif not visited[i] and len(graph[i]) > 1:
            cnt, visited = dfs(graph, i, visited)
            if cnt % 2 != 0:
                f = True
    if f:
        print('No')
    else:
        print('Yes')
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
