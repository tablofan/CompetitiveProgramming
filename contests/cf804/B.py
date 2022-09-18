def solve():
    n, m = map(int, input().split())
    res = ["" for _ in range(n)]
    m //= 2
    n //= 2
    b = True
    for i in range(n):
        for j in range(m):
            if b:
                res[i*2] += "10"
                res[i*2+1] += "01"
            else:
                res[i*2] += "01"
                res[i*2+1] += "10"
            b = not b
        if res[i*2][0] == "1":
            b = False
        else:
            b = True
    for i in res:
        print(*list(i))

    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
