def solve():
    n = int(input())
    a, b = [], []
    for _ in range(n):
        c, d = map(int, input().split())
        a.append(c)
        b.append(d)
    print(max(max(a), 0)*2 + abs(min(min(a), 0))*2 + max(max(b), 0)*2 + abs(min(min(b), 0))*2)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()