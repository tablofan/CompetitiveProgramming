def solve():
    n = int(input())
    if n%2 == 1:
        print(-1)
    else:
        print(f'{n//2} {0} {0}')
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
