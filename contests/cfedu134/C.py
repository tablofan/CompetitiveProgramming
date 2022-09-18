from bisect import bisect_left
def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(*[b[bisect_left(b, i)] - i for i in a])
    b = [0] + b
    bad = []
    for x, y in zip(a, b):
        if x > y:
            bad.append(y)
    bad.append(b[-1])
    print(*[bad[bisect_left(bad, i)] - i for i in a])
    return


for _ in range(int(input())):
    solve()