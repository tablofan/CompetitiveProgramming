def solve():
    a, b, c, d = map(int, input().split())
    if a*d == b*c:
        return 0
    if not a or not c:
        return 1
    if not (a*d)%(b*c) or not (b*c)%(a*d):
        return 1
    return 2


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
