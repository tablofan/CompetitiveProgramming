#G
grid = [[1 for _ in range(10)] for _ in range(10)]
for _ in range(int(input())):
    n = [int(i)-1 for i in input().split()]
    for i in n[:3]:
        grid[i] = [0 for _ in range(10)]
    for j in n[3:]:
        for i in grid:
            i[j] = 0
    grid = [[i+1 for i in j] for j in grid]
for i in grid:
    print(" ".join([str(k) for k in i]))