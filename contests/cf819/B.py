def solve():
    n, m = map(int, input().split())
    if n > m:
        print("No")
        return
    if m&1 and not n&1:
        print("No")
        return
    print("Yes")
    if n&1:
        res = [1]*(n-1) + [m-(n-1)]
        print(*res)
        return
    else:
        res = [1]*(n-2) + [(m-(n-2))//2]*2
        print(*res)
        return


for _ in range(int(input())):
    solve()