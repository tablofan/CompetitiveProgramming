def solve():
    def rotate(arr):
        return [arr[1], m - arr[0]]
    size = int(input())
    grid = [[int(i) for i in list(input())] for _ in range(size)]
    m = size-1
    res = 0
    x = -(-size//2)
    y = x
    if size%2:
        y -= 1
    for i in range(x):
        for j in range(y):
            pa = rotate([i,j])
            pb = rotate(pa)
            pc = rotate(pb)
            c = sum([grid[i][j], grid[pa[0]][pa[1]], grid[pb[0]][pb[1]], grid[pc[0]][pc[1]]])
            res += min(4-c, c)
    print(res)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
