def solve():
    n, m = map(int, input().split())
    res = 1
    if not n&1:
        res ^= 1
    if not m&1:
        res ^= 1
    return "Tonya" if res else "Burenka"


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
