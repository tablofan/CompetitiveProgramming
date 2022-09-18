def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    res = max(max(a) - a[0], a[-1] - min(a))
    for i,v in enumerate(a[1:]):
        res = max(res, a[i]-v)
    print(res)
    return


for _ in range(int(input())):
    solve()