# K
def bfs(raw):
    v = [[False for _ in range(9)] for _ in range(9)]
    groups = []
    q = []
    for i in range(9):
        for j in range(9):
            if not v[i][j]:
                q.append((i,j))
                curr = set()
                while q:
                    r,c = q.pop(0)
                    v[r][c] = True
                    curr.add((r,c))
                    if c!=8:
                        if raw[r*2+1][(c+1)*2]==" " and not v[r][c+1]:
                            q.append((r,c+1))
                    if r!=8:
                        if raw[(r+1)*2][c*2+1]==" " and not v[r+1][c]:
                            q.append((r+1,c))
                    if c!=0:
                        if raw[r*2+1][c*2]==" " and not v[r][c-1]:
                            q.append((r,c-1))
                    if r!=0:
                        if raw[r*2][c*2+1]==" " and not v[r-1][c]:
                            q.append((r-1,c))
                groups.append(curr)
    return groups


def cages(groups, nums):
    for i in groups:
        if len(set([nums[a][b] for a,b in i])) != len(i):
            return False
    for _ in range(len(groups)):
        x, y, s = map(int, input().split())
        groupsum = 0
        for i in groups:
            if (x - 1, y - 1) in i:
                for a, b in i:
                    groupsum += nums[a][b]
                break
        if groupsum != s:
            return False
    return True


def check(nums):
    good = [1,2,3,4,5,6,7,8,9]
    for i in nums:
        if sorted(i)!=good:
            return False
    for i in range(9):
        if sorted([row[i] for row in nums]) != good:
            return False
    for i in range(3):
        for j in range(3):
            s = [nums[i*3][j*3],nums[i*3+1][j*3],nums[i*3+2][j*3],nums[i*3][j*3+1],nums[i*3+1][j*3+1],nums[i*3+2][j*3+1],nums[i*3][j*3+2],nums[i*3+1][j*3+2],nums[i*3+2][j*3+2]]
            if sorted(s) != good:
                return False
    return True


raw = []
for _ in range(19):
    raw.append(input())
nums = [[int(j) for j in i if j.isnumeric()] for i in raw[1::2]]
for i in range(len(raw)):
    raw[i] = raw[i].replace("---","x")
    raw[i] = raw[i].replace(" | ", "x")
    raw[i] = raw[i].replace("| ", "x")
    raw[i] = raw[i].replace(" |","x")
    raw[i] = raw[i].replace("   "," ")
groups = bfs(raw)
print("OK") if (cages(groups, nums) and check(nums)) else print("NotOK")
