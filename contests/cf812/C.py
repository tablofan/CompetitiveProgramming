from bisect import bisect_left
def solve(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    if n == 1:
        return [1, 0]
    s = squares[bisect_left(squares, n)]
    a = [i for i in range(n, s-n-1, -1)]
    return solve(s-n-1) + [i for i in range(n, s-n-1, -1)]


def main():
    for _ in range(int(input())):
        n = int(input())
        res = solve(n-1)
        print(*res)
    return


if __name__ == "__main__":
    squares = [i * i for i in range(320)]
    main()