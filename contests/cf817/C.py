from collections import Counter
def solve():
    n = int(input())
    a = input().split()
    b = input().split()
    c = input().split()
    d = Counter(a+b+c)
    ra, rb, rc = 0, 0, 0
    for x,y,z in zip(a,b,c):
        if d[x] == 2:
            ra += 1
        if d[x] == 1:
            ra += 3
        if d[y] == 2:
            rb += 1
        if d[y] == 1:
            rb += 3
        if d[z] == 2:
            rc += 1
        if d[z] == 1:
            rc += 3
    print(*[ra, rb, rc])
    return


for _ in range(int(input())):
    solve()