def solve():
    n, m = map(int, input().split())
    a = [[int(i) for i in input()] for _ in range(n)]
    def find():
        z = 0
        for i in range(n):
            for j in range(m):
                if not a[i][j]:
                    z = max(z, 1)
                    for c, d in [(0,1), (0,-1), (-1,0), (1,0), (1,1), (-1,-1), (1,-1), (-1,1)]:
                        if 0 <= i+c < n and 0 <= j+d < m and not a[i+c][j+d]:
                            return 2
        return z
    z = find()
    print(sum(map(sum, a))-2+z)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
