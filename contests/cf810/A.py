def solve():
    n = int(input())
    for i in range(1, n):
        print(i+1, end=" ")
    print(1)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
