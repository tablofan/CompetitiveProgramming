def solve():
    n = int(input())
    d = [int(i) for i in input().split()]
    n -= 1
    if d[n] == 0:
        return "NO"
    n = d[n]-1
    if d[n] == 0:
        return "NO"
    return "YES"


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
