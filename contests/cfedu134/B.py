def solve():
    n, m, sx, sy, d = map(int, input().split())
    if sx+d >= n and sx-d <= 1:
        return -1
    if sy+d >= m and sy-d <= 1:
        return -1
    if sx+d >= n and sy+d >= m:
        return -1
    if sx-d <= 1 and sy-d <= 1:
        return -1
    return n + m - 2


for _ in range(int(input())):
    print(solve())