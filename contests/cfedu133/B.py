def solve():
    n = int(input())
    a = [i+1 for i in range(n)]
    print(n)
    print(*a)
    for i in range(1, n):
        a[i-1], a[i] = a[i], a[i-1]
        print(*a)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
