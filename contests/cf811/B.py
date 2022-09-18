def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    s = set()
    for i in a[::-1]:
        if i in s:
            return n - len(s)
        s.add(i)
    return 0


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
