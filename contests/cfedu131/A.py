def solve():
    a = map(int, input().split())
    b = map(int, input().split())
    c = sum(a) + sum(b)
    if c == 0:
        print(0)
    elif c == 1 or c == 2 or c == 3:
        print(1)
    else:
        print(2)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
