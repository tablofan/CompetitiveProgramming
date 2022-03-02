# F
from collections import deque
row,col = map(int, input().split())
grid = []
for _ in range(row):
    grid.append(input())
for i in range(row):
    for j in range(col):
        if grid[i][j] == 'A':
            r = i
            c = j
            break

seen = {(r,c)}
starts = []
res = []
thisvariableisimportant = False

if r != row - 1:
    if grid[r + 1][c] == '.':
        starts.append((r+1,c,0))
    elif grid[r + 1][c] == 'O':
        starts.append((r+1,c,1))
    if grid[r + 1][c] == 'A':
        thisvariableisimportant = True
if r != 0:
    if grid[r - 1][c] == '.':
        starts.append((r-1,c,0))
    elif grid[r - 1][c] == 'O':
        starts.append((r-1,c,1))
    if grid[r-1][c] == 'A':
        thisvariableisimportant = True
if c != col - 1:
    if grid[r][c+1] == '.':
        starts.append((r,c+1,0))
    elif grid[r][c+1] == 'O':
        starts.append((r,c+1,1))
    if grid[r][c+1] == 'A':
        thisvariableisimportant = True
if c != 0:
    if grid[r][c-1] == '.':
        starts.append((r,c-1,0))
    elif grid[r][c-1] == 'O':
        starts.append((r,c-1,1))
    if grid[r][c-1] == 'A':
        thisvariableisimportant = True
startr = r
startc = c

for start in starts:
    seen = {(start[0],start[1]), (startr,startc)}
    q0 = deque()
    q1 = deque()
    reachable = 0
    weight = 0
    final = -1
    reached = False
    if start[2] == 0:
        q0.append((start[0],start[1]))
    if start[2] == 1:
        q1.append((start[0], start[1]))
        reachable += 1
    while q0 or q1:
        if q0:
            r,c = q0.popleft()
            if r!=row-1 and (r+1,c) not in seen:
                if grid[r+1][c] == '.':
                    q0.append((r+1,c))
                    seen.add((r+1,c))
                elif grid[r+1][c] == 'O':
                    reachable += 1
                    q1.append((r+1,c))
                    seen.add((r + 1, c))
                elif grid[r+1][c] == 'A':
                    final = weight if final==-1 else final
                    reached = True
            if r!=0 and (r-1,c) not in seen:
                if grid[r-1][c] == '.':
                    q0.append((r-1,c))
                    seen.add((r-1,c))
                elif grid[r-1][c] == 'O':
                    reachable += 1
                    q1.append((r-1,c))
                    seen.add((r - 1, c))
                elif grid[r-1][c] == 'A':
                    final = weight if final==-1 else final
                    reached = True
            if c!=col-1 and (r,c+1) not in seen:
                if grid[r][c+1] == '.':
                    q0.append((r,c+1))
                    seen.add((r, c+1))
                elif grid[r][c+1] == 'O':
                    reachable += 1
                    q1.append((r,c+1))
                    seen.add((r, c+1))
                elif grid[r][c+1] == 'A':
                    final = weight if final==-1 else final
                    reached = True
            if c!=0 and (r,c-1) not in seen:
                if grid[r][c-1] == '.':
                    q0.append((r,c-1))
                    seen.add((r, c-1))
                elif grid[r][c-1] == 'O':
                    reachable += 1
                    q1.append((r,c-1))
                    seen.add((r, c-1))
                elif grid[r][c-1] == 'A':
                    final = weight if final==-1 else final
                    reached = True
        else:
            weight+=1
            q0 = q1.copy()
            q1.clear()

    if not reached:
        final = 0
    temp = 1
    temp += final//2
    if final % 2 > reachable - final or reached == False:
        res.append(0)
    elif final%2:
        res.append(temp+1)
    else:
        res.append(temp)
if thisvariableisimportant:
    print(1)
elif any(res):
    print(min(i for i in res if i != 0))
else:
    print(-1)