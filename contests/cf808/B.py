def ro(l, i):
    if not i:
        return l
    rem = l%i
    if not rem:
        return l
    return l+i-rem


def solve():
    n, l, r = map(int, input().split())
    res = []
    d = r - l
    can = True
    for i in range(1, n+1):
        rem = ro(l, i)
        if rem > r:
            can = False
            break
        res.append(rem)
    if not can:
        print("NO")
    else:
        print("YES")
        print(*res)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()