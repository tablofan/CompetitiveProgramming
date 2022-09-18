def solve():
    n, k, b, s = map(int, input().split())
    _max = n*(k-1)+b*k
    _min = b*k
    if s > _max or s < _min:
        print(-1)
        return
    a = [0]*(n-1) + [b*k]
    # print(a)
    diff = s - b*k
    i = 0
    while diff > 0:
        a[i] += min(diff, k-1)
        diff -= (k-1)
        i += 1
    print(*a)
    return


for _ in range(int(input())):
    solve()
