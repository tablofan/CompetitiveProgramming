def solve():
    n = int(input())
    arr = [int(i) for i in input().split()]
    ssf = 0
    start = 0
    for i,v in enumerate(arr):
        if ssf > 0:
            if v > 0:
                start = v

    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
