#A
# k = list(map(int,input().split()))[1]
# n = [int(i) for i in input().split()]
# res = 0
# rem = 0
# for i in n:
#
#     if i<=rem:
#         rem -= i
#     else:
#         res += (i//k)
#         if i%k:
#             res += 1
#         rem = (k - i%k)%k
# print(res)


#B
#Maths
# import math
# def solve(a, b, c, d):
#     f = ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0
#     g = (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a ** 2.0)) + (27.0 * d / a)) / 27.0
#     h = ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)
#     if h > 0:
#         R = -(g / 2.0) + math.sqrt(h)
#         if R >= 0:
#             S = R ** (1 / 3.0)
#         else:
#             S = (-R) ** (1 / 3.0) * -1
#         T = -(g / 2.0) - math.sqrt(h)
#         if T >= 0:
#             U = (T ** (1 / 3.0))
#         else:
#             U = ((-T) ** (1 / 3.0)) * -1
#         return (S + U) - (b / (3.0 * a))
#     return "error"
#
# n,T,v,d = map(int,input().split())
# theta = 0
# x,y,s = map(float,input().split())
# z = s*(abs((1 - x**2 - y**2))**(1/2))
# for _ in range(n-1):
#     tx, ty, ts = map(float,input().split())
#     tz = ts*(abs((1 - tx**2 - ty**2))**(1/2))
#     theta += math.acos(tx*x+ty*y+tz*z)
#     x,y,z = tx,ty,tz
# if theta == 0:
#     print(0.0)
# else:
#     x = (d/theta)**3
#     t = solve(x,-3*x*T,3*x*T*T+(3/(4*math.pi))*v,1-x*T*T*T)
#     r = (1+(3/(4*math.pi))*v*t)**(1/3)
#     print(r*theta)

#Binary Search
# import math
# n,T,v,d = map(int,input().split())
# theta = 0
# x,y,s = map(float,input().split())
# z = s*(abs((1 - x**2 - y**2))**(1/2))
# for _ in range(n-1):
#     tx, ty, ts = map(float,input().split())
#     tz = ts*(abs((1 - tx**2 - ty**2))**(1/2))
#     theta += math.acos(tx*x+ty*y+tz*z)
#     x,y,z = tx,ty,tz
# c1 = theta/d
# c2 = (3*v)/(4*math.pi)
#
# def b(l,r,t):
#     res = ((1+c2*t)**(1/3))*c1+t
#     if res < T+0.000000001 and res>T-0.000000001:
#         return t
#     if res>T:
#         return b(l,t,(l+t)/2)
#     return b(t,r,(r+t)/2)
#
# res = b(0,T,T/2)
# print(((1+c2*res)**(1/3))*theta)

#C
# n = int(input())
# p = [int(i) for i in input().split()]
# low = p[0]-1
# res = []
# for i in p:
#     low = min(low+1,i)
#     res.append(str(low))
# print(" ".join(res))

#D
# n, h, v, w = map(int, input().split())
# nearest = 1 << (h - 1).bit_length()
# tree = [0 for _ in range(2 * nearest)]
#
#
# def update(node,nodelow, nodehigh, updatelow, updatehigh):
#     if updatelow <= nodelow and updatehigh >= nodehigh:
#         tree[node] = 1
#         return
#     if nodehigh < updatelow or nodelow > updatehigh:
#         return
#     lastinleft = (nodelow + nodehigh)//2
#     update(2*node, nodelow, lastinleft, updatelow, updatehigh)
#     update(2*node+1, lastinleft+1, nodehigh, updatelow, updatehigh)
#     return
#
#
# def query(root):
#     if tree[root]:
#         return True
#     if root>nearest:
#         return False
#     return query(2*root) and query(2*root+1)
#
#
# if v*w >= h:
#     print("GAME OVER")
# else:
#     update(1, 0, nearest-1, h,nearest-1)
#     for _ in range(n):
#         c,r = map(int,input().split())
#         start = (r + c*v)%h
#         end = (start+w*v)%h
#         if start > end:
#             update(1, 0, nearest-1,start, h-1)
#             update(1, 0, nearest-1, 0, end)
#         else:
#             update(1, 0, nearest-1, start, end)
#     print("GAME OVER") if query(1) else print("VICTORY")


#E
# n, t = map(int,input().split())
# n -= 2
# dp = [0 for _ in range(-(-(n)//2-1)-1)]
# for i in range(1,len(dp)):
#     dp[i] = dp[i-1]+(n-len(dp)-i+1)*9*(10**(i-1))
# if t>dp[-1]:
#     print(-1)
# else:
#     for i,v in enumerate(dp):
#         if t<=v:
#             d = i
#             break
#     temp = n
#     while len(dp)>2:
#         temp -= 2
#         dp = [0 for _ in range(-(-(temp) // 2 - 1) - 1)]
#         for i in range(1, len(dp)):
#             dp[i] = dp[i - 1] + (n - len(dp) - i + 1) * 9 * (10 ** (i - 1))
#         for i, v in enumerate(dp):
#             if t <= v:
#                 d = min(d,i)
#                 break
#     dp = [0 for _ in range(d)]
#     for i in range(1, d):
#         dp[i] = dp[i-1]+(n-d-i)*9*(10**(i-1))
#     res = -(-(t-dp[-1])//(n-d*2))
#     res += int("9"*(d-1)) if d>1 else 0
#     print(res)

#F
# from collections import deque
# row,col = map(int, input().split())
# grid = []
# for _ in range(row):
#     grid.append(input())
# for i in range(row):
#     for j in range(col):
#         if grid[i][j] == 'A':
#             r = i
#             c = j
#             break
#
# seen = {(r,c)}
# starts = []
# res = []
# thisvariableisimportant = False
#
# if r != row - 1:
#     if grid[r + 1][c] == '.':
#         starts.append((r+1,c,0))
#     elif grid[r + 1][c] == 'O':
#         starts.append((r+1,c,1))
#     if grid[r + 1][c] == 'A':
#         thisvariableisimportant = True
# if r != 0:
#     if grid[r - 1][c] == '.':
#         starts.append((r-1,c,0))
#     elif grid[r - 1][c] == 'O':
#         starts.append((r-1,c,1))
#     if grid[r-1][c] == 'A':
#         thisvariableisimportant = True
# if c != col - 1:
#     if grid[r][c+1] == '.':
#         starts.append((r,c+1,0))
#     elif grid[r][c+1] == 'O':
#         starts.append((r,c+1,1))
#     if grid[r][c+1] == 'A':
#         thisvariableisimportant = True
# if c != 0:
#     if grid[r][c-1] == '.':
#         starts.append((r,c-1,0))
#     elif grid[r][c-1] == 'O':
#         starts.append((r,c-1,1))
#     if grid[r][c-1] == 'A':
#         thisvariableisimportant = True
# startr = r
# startc = c
#
# for start in starts:
#     seen = {(start[0],start[1]), (startr,startc)}
#     q0 = deque()
#     q1 = deque()
#     reachable = 0
#     weight = 0
#     final = -1
#     reached = False
#     if start[2] == 0:
#         q0.append((start[0],start[1]))
#     if start[2] == 1:
#         q1.append((start[0], start[1]))
#         reachable += 1
#     while q0 or q1:
#         if q0:
#             r,c = q0.popleft()
#             if r!=row-1 and (r+1,c) not in seen:
#                 if grid[r+1][c] == '.':
#                     q0.append((r+1,c))
#                     seen.add((r+1,c))
#                 elif grid[r+1][c] == 'O':
#                     reachable += 1
#                     q1.append((r+1,c))
#                     seen.add((r + 1, c))
#                 elif grid[r+1][c] == 'A':
#                     final = weight if final==-1 else final
#                     reached = True
#             if r!=0 and (r-1,c) not in seen:
#                 if grid[r-1][c] == '.':
#                     q0.append((r-1,c))
#                     seen.add((r-1,c))
#                 elif grid[r-1][c] == 'O':
#                     reachable += 1
#                     q1.append((r-1,c))
#                     seen.add((r - 1, c))
#                 elif grid[r-1][c] == 'A':
#                     final = weight if final==-1 else final
#                     reached = True
#             if c!=col-1 and (r,c+1) not in seen:
#                 if grid[r][c+1] == '.':
#                     q0.append((r,c+1))
#                     seen.add((r, c+1))
#                 elif grid[r][c+1] == 'O':
#                     reachable += 1
#                     q1.append((r,c+1))
#                     seen.add((r, c+1))
#                 elif grid[r][c+1] == 'A':
#                     final = weight if final==-1 else final
#                     reached = True
#             if c!=0 and (r,c-1) not in seen:
#                 if grid[r][c-1] == '.':
#                     q0.append((r,c-1))
#                     seen.add((r, c-1))
#                 elif grid[r][c-1] == 'O':
#                     reachable += 1
#                     q1.append((r,c-1))
#                     seen.add((r, c-1))
#                 elif grid[r][c-1] == 'A':
#                     final = weight if final==-1 else final
#                     reached = True
#         else:
#             weight+=1
#             q0 = q1.copy()
#             q1.clear()
#
#     if not reached:
#         final = 0
#     temp = 1
#     temp += final//2
#     if final % 2 > reachable - final or reached == False:
#         res.append(0)
#     elif final%2:
#         res.append(temp+1)
#     else:
#         res.append(temp)
# if thisvariableisimportant:
#     print(1)
# elif any(res):
#     print(min(i for i in res if i != 0))
# else:
#     print(-1)

#G
# grid = [[1 for _ in range(10)] for _ in range(10)]
# for _ in range(int(input())):
#     n = [int(i)-1 for i in input().split()]
#     for i in n[:3]:
#         grid[i] = [0 for _ in range(10)]
#     for j in n[3:]:
#         for i in grid:
#             i[j] = 0
#     grid = [[i+1 for i in j] for j in grid]
# for i in grid:
#     print(" ".join([str(k) for k in i]))

#H
from functools import cache


def main():
    l, r, t = map(int, input().split())
    t //= 100
    # if (r-l)<t:
    #     return (r+l)/2


    print(t)
    @cache
    def dfs(l, r, curr, t):
        print(f'l:{l} r:{r} curr:{curr} t:{t}')
        if not t:
            return (r - curr + 1) * curr
        m = 0
        for i in range(l, curr):
            m = max(m, dfs(l, curr - 1, i, t - 1))
        return (r - curr + 1) * curr + m

    m = 0
    for i in range(l,r+1):
        m = max(m, dfs(l,r,i,t-1))
    print(m)
    return m/(r-l+1)

if __name__ == "__main__":
    print(main())

#I
# from collections import defaultdict
# s1 = input()
# s2 = input()
# mapping = defaultdict(set)
# for i,v in enumerate(s1[:-1]):
#     mapping[v].add((s1[i+1],i))
# print(mapping)
#
# res = 1
# for i in s2:
#     pass

#J
# n = int(input())
# x = ["a","b"]
# print(f"1 2 {x[n%2]}")
# for i in range(3,n+1):
#     print(" ".join([x[(n-i+1)%2], str(i),x[(n-i)%2]]))

#K
# def bfs(raw):
#     v = [[False for _ in range(9)] for _ in range(9)]
#     groups = []
#     q = []
#     for i in range(9):
#         for j in range(9):
#             if not v[i][j]:
#                 q.append((i,j))
#                 curr = set()
#                 while q:
#                     r,c = q.pop(0)
#                     v[r][c] = True
#                     curr.add((r,c))
#                     if c!=8:
#                         if raw[r*2+1][(c+1)*2]==" " and not v[r][c+1]:
#                             q.append((r,c+1))
#                     if r!=8:
#                         if raw[(r+1)*2][c*2+1]==" " and not v[r+1][c]:
#                             q.append((r+1,c))
#                     if c!=0:
#                         if raw[r*2+1][c*2]==" " and not v[r][c-1]:
#                             q.append((r,c-1))
#                     if r!=0:
#                         if raw[r*2][c*2+1]==" " and not v[r-1][c]:
#                             q.append((r-1,c))
#                 groups.append(curr)
#     return groups
#
#
# def cages(groups, nums):
#     for i in groups:
#         if len(set([nums[a][b] for a,b in i])) != len(i):
#             return False
#     for _ in range(len(groups)):
#         x, y, s = map(int, input().split())
#         groupsum = 0
#         for i in groups:
#             if (x - 1, y - 1) in i:
#                 for a, b in i:
#                     groupsum += nums[a][b]
#                 break
#         if groupsum != s:
#             return False
#     return True
#
#
# def check(nums):
#     good = [1,2,3,4,5,6,7,8,9]
#     for i in nums:
#         if sorted(i)!=good:
#             return False
#     for i in range(9):
#         if sorted([row[i] for row in nums]) != good:
#             return False
#     for i in range(3):
#         for j in range(3):
#             s = [nums[i*3][j*3],nums[i*3+1][j*3],nums[i*3+2][j*3],nums[i*3][j*3+1],nums[i*3+1][j*3+1],nums[i*3+2][j*3+1],nums[i*3][j*3+2],nums[i*3+1][j*3+2],nums[i*3+2][j*3+2]]
#             if sorted(s) != good:
#                 return False
#     return True
#
#
# raw = []
# for _ in range(19):
#     raw.append(input())
# nums = [[int(j) for j in i if j.isnumeric()] for i in raw[1::2]]
# for i in range(len(raw)):
#     raw[i] = raw[i].replace("---","x")
#     raw[i] = raw[i].replace(" | ", "x")
#     raw[i] = raw[i].replace("| ", "x")
#     raw[i] = raw[i].replace(" |","x")
#     raw[i] = raw[i].replace("   "," ")
# groups = bfs(raw)
# print("OK") if (cages(groups, nums) and check(nums)) else print("NotOK")



#L
# from collections import defaultdict, deque
# groups = []
# d = defaultdict(int)
#
#
# def dfs(l,r,i):
#     if (l,r,i) in d:
#         return d[(l,r,i)]
#     if l<0 or r<0:
#         return -1
#     if i==len(groups):
#         return r+l
#     left = dfs(l - groups[i][0], r - groups[i][1], i + 1)
#     d[(l - groups[i][0], r - groups[i][1], i + 1)] = left
#     right = dfs(l-groups[i][1],r-groups[i][0],i+1)
#     d[(l-groups[i][1],r-groups[i][0],i+1)] = right
#     return max(left,right)
#
#
# def main():
#     l,r,n,c = map(int,input().split())
#     graph = []
#     for _ in range(c):
#         graph.append(sorted([int(i) for i in input().split()]))
#     graph.sort(key=lambda x:[x[0],x[1]])
#     adj = dict()
#     for i in range(n):
#         adj[i] = []
#     for a,b in graph:
#         adj[a].append(b)
#         adj[b].append(a)
#     v = [0 for _ in range(n)]
#     lq = deque()
#     rq = deque()
#     free = 0
#     for i in range(n):
#         if not v[i]:
#             left = 1
#             right = 0
#             lq.append(i)
#             v[i] = 1
#             while lq or rq:
#                 for curr in lq:
#                     for j in adj[curr]:
#                         if v[curr] == v[j]:
#                             return "No"
#                         if not v[j]:
#                             # print(f"curr:{curr} j:{j} v[j]:{v[j]} left:{left} right:{right}")
#                             rq.append(j)
#                             right += 1
#                             v[j] = 2
#                 lq.clear()
#                 for curr in rq:
#                     v[curr] = 2
#                     for j in adj[curr]:
#                         if v[curr] == v[j]:
#                             return "No"
#                         if not v[j]:
#                             # print(f"curr:{curr} j:{j} v[j]:{v[j]} left:{left} right:{right}")
#                             lq.append(j)
#                             left += 1
#                             v[j] = 1
#                 rq.clear()
#             if left == 1 and right == 0:
#                 free += 1
#             else:
#                 groups.append((left,right))
#     # print(v)
#     # print(groups)
#     return "Yes" if dfs(l,r,0)>=free else "No"
#
#
# if __name__=="__main__":
#     print(main())