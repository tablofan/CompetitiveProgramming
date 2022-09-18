def solve():
    n = int(input())
    s = [int(i) for i in input().split()]
    e = [int(i) for i in input().split()]
    res = [e[0] - s[0]]
    for i in range(1, n):
        if s[i] < e[i-1]:
            res.append(e[i] - e[i-1])
        else:
            res.append(e[i] - s[i])
    print(" ".join([str(i) for i in res]))
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
