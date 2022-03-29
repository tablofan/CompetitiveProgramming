def solve():
    return


def main():
    n, m = map(int, input().split())
    grid = []
    moves = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    v = set()
    covered = set()
    for _ in range(n):
        grid.append(input())
    for i in n:
        for j in m:
            if grid[i][j] == 'R':
                start = (i, j)
            if grid[i][j] == 'T':
                end = (i, j)
            if grid[i][j] == 'K':
                cantake = True
                tmoves = set()
                for a, b in moves:
                    if 0 <= i + a < n and 0 <= j + b < m:
                        if grid[i + a][j + b] == 'K':
                            cantake = False
                        else:
                            tmoves.add((i+a, j+b))
                if not cantake:
                    v.add((i, j))
                    covered.union(tmoves)
    q = [start]
    moves = [(1,0), (-1,0), (0,-1), (0, 1)]
    while q:
        r, c = q.pop()
        for a,b in moves:
            if 0 <= r + a < n and 0 <= c + b < m and (r+a, c+b) not in v:
                if (r+a,c+b) in covered:

                q.append((r+a, c+b))


    return


if __name__ == "__main__":
    main()
