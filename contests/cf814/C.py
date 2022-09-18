def solve():
    n, q = map(int, input().split())
    a = [int(i) for i in input().split()]
    s = [(0, a[0])]
    c = [0]
    if a[0] != n:
        for i,v in enumerate(a[1:]):
            # print(f'{s = }')
            while s and v>s[-1][1]:
                c[s[-1][0]] += i-s[-1][0]
                s.pop()
            s.append((i + 1, v))
            c.append(1 if len(s)==1 else 0)
            if v == n:
                break
    print(f'{a = }')
    print(f'{c = }')
    for _ in range(q):
        ind, k = map(int, input().split())
        print(f'{a[ind-1]} {k}')
        if a[ind-1] == n:
            print(k - max(0, ind-2))
            continue
        if ind > len(c):
            print(0)
            continue
        m = max(0, ind - 2)
        k = max(0, k-m)
        p = c[ind-1]
        print(min(p, k))

    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
