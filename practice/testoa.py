from itertools import product

def solve(grid, maxSum):
    n = len(grid)
    pre = [[0]*(n+1) for _ in range(n+1)]
    for i, j in product(range(n), range(n)):
        pre[i + 1][j + 1] = pre[i + 1][j] + pre[i][j + 1] - pre[i][j] + grid[i][j]
    def below(k):
        for i, j in product(range(n + 1 - k), range(n + 1 - k)):
            if pre[i + k][j + k] - pre[i][j + k] - pre[i + k][j] + pre[i][j] > maxSum:
                return False
        return True
    lo, hi = 1, n
    while lo <= hi:
        mid = (lo + hi) // 2
        if below(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

def main():
    grid = [[2,2,2],[3,3,3],[4,4,4]]
    maxSum = 15
    print(solve(grid, maxSum))

main()