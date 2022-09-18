def solve():
    n = int(input())
    a = input()
    r = sum(i if v=="L" else n-i-1 for i,v in enumerate(a))
    change = []
    for i,v in enumerate(a):
        curr = i if v=="L" else n-i-1
        change.append(max(i, n-i-1)-curr)
    change.sort(reverse=True)
    res = []
    for i in change:
        r += i
        res.append(r)
    print(*res)
    return


for _ in range(int(input())):
    solve()