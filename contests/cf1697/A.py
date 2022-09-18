def solve():
    n, m = map(int, input().split())
    s = sum([int(i) for i in input().split()])
    res = max(0, s-m)
    print(res)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
