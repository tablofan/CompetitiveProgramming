def solve():
    n = int(input())
    if n == 1:
        print(2)
    else:
        res = n//3
        if n%3:
            res += 1
        print(res)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
