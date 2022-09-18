def solve():
    n = int(input())
    if n%2:
        print("1", end=" ")
        print(*[a*2+b+1 for a in range(n//2) for b in range(2, 0, -1)])
    else:
        print(*[a*2+b for a in range(n//2) for b in range(2, 0, -1)])
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()