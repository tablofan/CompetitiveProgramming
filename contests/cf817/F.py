def solve():
    n,m = map(int, input().split())
    g = [[1 if i=="*" else 0 for i in input()] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if g[i][j]:
                t = 0
                for a,b in [(0,-1), (0,1), (1,0), (-1,0)]:
                    if 0<=i+a<n and 0<=j+b<m and g[i+a][j+b]:
                        t += 1
                for a,b in [(1,1), (-1,1), (-1,-1), (1,-1)]:
                    if 0 <= i + a < n and 0 <= j + b < m and g[i + a][j + b]:
                        t += 1
                        if not g[i+a][j] and not g[i][j+b]:
                            return "NO"
                if t!=2:
                    return "NO"
    return "YES"


for _ in range(int(input())):
    print(solve())