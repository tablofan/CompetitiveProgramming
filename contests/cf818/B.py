def solve():
    n, k, r, c = map(int, input().split())
    g = [["."]*n for _ in range(n)]
    r -= 1
    c -= 1
    r += c
    while r >= 0:
        r -= k
    r += k
    while r <= n*2:
        i = r
        j = 0
        for x in range(n):
            if 0 <= i < n and 0 <= j < n:
                g[i][j] = 'X'
            i -= 1
            j += 1
        r += k
        # print(f'{r = }')
    for i in g:
        print("".join(i))
    return


for _ in range(int(input())):
    solve()