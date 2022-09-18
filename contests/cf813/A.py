def solve():
    n, k = map(int, input().split())
    p = [int(i) for i in input().split()]
    res = 0
    for i in range(k):
        if p[i] > k:
            res += 1
    print(res)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()