def solve():
    n, k = map(int, input().split())
    arr = [int(i) for i in input().split()]
    t = []
    for i,v in enumerate(arr[:-1]):
        if arr[i+1]*2 > v:
            t.append(True)
        else:
            t.append(False)
    res = 0
    f = sum(1 if not i else 0 for i in t[:k])
    if f == 0:
        res += 1
    for i,v in enumerate(t[k:]):
        if not v:
            f += 1
        if not t[i]:
            f -= 1
        if not f:
            res += 1
    return res


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
