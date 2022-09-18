def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    print(a[-1]+a[-2]-a[0]-a[1])
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
