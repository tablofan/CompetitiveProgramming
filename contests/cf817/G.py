def flip(n):
    b = bin(n)
    return int("".join(["0" if i=="1" else "1" for i in b[2:]]))

def solve():
    n = int(input())
    m = 134217727
    o = []
    e = []
    while n > 6:
        o.append(m)
        o.append(flip(m))
        m -= 1
        e.append(m)
        e.append(flip(m))
        m -= 1
        n -= 4
    if n == 6:
        o.append(m)
        m -= 1
        e.append(m)
        e.append(flip(m))
        m -= 1
        e.append(m)
        m -= 1
        o.append(m)
        o.append(flip(m))
    if n == 5:
        o.append(m)
        o.append(flip(m))
        m -= 1
        e.append(m)
        e.append(flip(m))
        e.append(0)
    if n == 4:
        o.append(m)
        o.append(flip(m))
        m -= 1
        e.append(m)
        e.append(flip(m))
    if n == 3:
        o.append(m)
        m -= 1
        e.append(m)
        e.append(flip(m))
    print(e)
    print(o)
    re, ro = 0, 0
    for i in e:
        re ^= i
    for i in o:
        ro ^= i
    print(re)
    print(ro)
    return


for _ in range(int(input())):
    solve()