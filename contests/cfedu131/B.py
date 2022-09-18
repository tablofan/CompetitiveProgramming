def solve():
    n = int(input())
    s = set()
    res = []
    for i in range(1,n+1):
        j = i
        if j not in s:
            while (j < n+1) and (j not in s):

                s.add(j)
                res.append(j)
                j *= 2
    print(2)
    for i in range(1, n+1):
        if i not in s:
            res.append(i)
    print(*res)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
