def solve():
    n, x = map(int, input().split())
    h = [int(i) for i in input().split()]
    h.sort()
    for i in range(n):
        if h[i] + x > h[n+i]:
            return "NO"
    return "YES"


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
