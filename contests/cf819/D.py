from collections import defaultdict, deque
def solve():
    n, m = map(int, input().split())
    g = defaultdict(list)
    for i in range(m):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        g[a].append((b, i))
    res = [0 for _ in range(m)]
    s = deque([(min(g.keys()), 0)])
    v = set()
    while s:
        x, p = s.popleft()
        v.add(x)
        for a,b in g[x]:
            res[b] = p
            if a not in v:
                s.append((a, p^1))
    print(res)


    return


for _ in range(int(input())):
    solve()