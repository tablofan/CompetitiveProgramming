def solve():
    n = input()
    k = 10**(len(n)-1)
    print(int(n)-k)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()