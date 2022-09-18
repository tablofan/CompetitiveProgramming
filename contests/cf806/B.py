def solve():
    n = int(input())
    inp = list(input())
    s = set(inp)
    print(n+len(s))
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
