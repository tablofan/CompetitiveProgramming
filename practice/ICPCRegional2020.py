#A
# fb = [1,1,1,0,1,0,0,1,0,0]
# print("".join(["buzz","fizz"][fb[i]] for i in range(int(input()))))

#B
# a,b = input().split()
# for i,v in enumerate(b):
#     if int(a) > int(v):
#         print(b[:i]+a+b[i:])
#         break
#     if i == len(b)-1:
#         print(b+a)

#C
# r,c,n = map(int, input().split())
# for _ in range(r):
#     if 2*n>c:
#         row = [1 if i == 'o' else 0 for i in input()]
#         temp = row[:2*n-c]
#         for i in range(c-n):
#             temp.append(row[2*n-c+i] and row[c-i-1])
#     else:
#         row = [1 if i == 'o' else 0 for i in input()]
#         temp = list(reversed(row[2*n:]))
#         for i in range(n):
#             temp.append(row[i] and row[2*n-i-1])
#     print("".join(['o' if i else 'x' for i in temp]))

#D


#E
# s, k = input().split()
# k = int(k)
# s += 'X'*((k - (len(s) % k)) % k)
# n = len(s)//k
# ans = ""
# for i in range(n):
#     for j in range(k):
#         ans += s[j*n+i]
# print(ans)


#F
# n = int(input())
# #Create adjacency list
# graph = [[] for _ in range(n + 1)]
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     graph[a-1].append(b-1)
#
# #Topological sort while keeping track of distance
# #Kahn's algorithm
# indegree = [0 for _ in range(n)]
# dist = [0 for _ in range(n)]
# q = []
#
# #Find nodes that do not have prerequisites and add to queue
# for i in graph:
#     for j in i:
#         indegree[j] += 1
# for i,v in enumerate(indegree):
#     if not v:
#         q.append(i)
#
# #Index is to detect cycles in the graph
# #If index != number of nodes, then you know that some nodes didn't get looked at
# #Only way for this to happen is if there are cycles in the dag
# index = 0
# while q:
#     at = q.pop(0)
#     index += 1
#     for i in graph[at]:
#         indegree[i] -= 1
#         dist[i] = 1 + dist[at]
#         if not indegree[i]:
#             q.append(i)
# if index != n:
#     print(-1)
# else:
#     print(max(dist)+1)


#G
# n = []
# diff = int(10e9)
# for _ in range(int(input())):
#     n.append(int(input()))
# n.sort()
# for i,v in enumerate(n[1:]):
#     diff = min(v-n[i], diff)
# print(0) if diff == int(10e9) else print(diff)


#H
# def gcd(a, b):
#     while b:
#         a, b = b, a%b
#     return a
# a,b = map(int, input().split())
# x = gcd(a,b) if gcd(a,b) != 1 else int(10e10)
# if x!= int(10e10):
#     for i in range(2,100000):
#         if x%i == 0:
#             x = i
#             break
# total = []
# n = 2
# while n < int(a**(0.5))+1:
#     if a%n:
#         n += 1
#     else:
#         total.append(n)
#         break
# if not total:
#     total.append(a)
# n = 2
# while n < int(b**(0.5))+1:
#     if b%n:
#         n += 1
#     else:
#         total.append(n)
#         break
# if len(total) == 1:
#     total.append(b)
# print(min(x,sum(total)))



#I
# n = int(input())
# m = []
# for _ in range(n):
#     m.append([0 if i=='#' else 1 for i in input()])
# q = [(0,0,1)]
# m[n-1][n-1] = 2
# steps = 2
# while q:
#     r,c,l = q.pop(0)
#     steps += 2
#     m[r][c] = 0
#     if r!=n-1:
#         if m[r+1][c]:
#             if m[r+1][c]==2:
#                 path = l+1
#             else:
#                 q.append((r+1,c,l+1))
#     if c!=n-1:
#         if m[r][c+1]:
#             if m[r][c+1]==2:
#                 path = l+1
#             else:
#                 q.append((r, c+1, l+1))
#     if r!=0:
#         if m[r-1][c]:
#             q.append((r-1,c,l+1))
#     if c!=0:
#         if m[r][c-1]:
#             q.append((r,c-1,l+1))
# print(steps-path)

#J

#K
# n = int(input())
# coords = []
# for _ in range(n):
#     coords.append([int(i) for i in input().split()])
# d = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             d[i][j] = int(10e10)
#         else:
#             d[i][j] = (abs(coords[i][0]-coords[j][0])**2+abs(coords[i][1]-coords[j][1])**2)
# c = [i[:] for i in d]
# for _ in range(n//2):
#     m = min([min(row) for row in d])
#     b = False
#     for i,v in enumerate(d):
#         for j,k in enumerate(v):
#             if k == m:
#                 c[i][j] = int(10e10)
#                 c[j][i] = int(10e10)
#                 d[i] = [int(10e10) for _ in range(n)]
#                 d[j] = [int(10e10) for _ in range(n)]
#                 for index in range(n):
#                     d[index][i] = int(10e10)
#                     d[index][j] = int(10e10)
#                 b = True
#                 break
#         if b:
#             break
# print(min([min(row) for row in c]))

#L
# n = int(input())
# vol = [int(i) for i in input().split()]
# m = -1
# for _ in range(n):
#     tempsum = 0
#     temp = input()
#     for i in temp:
#         tempsum += vol[int(i)]
#     if tempsum>m:
#         m = tempsum
#         ans = temp
# print(ans)


#M
# r,c = map(int, input().split())
# grid = []
# for _ in range(r):
#     grid.append(list(input()))
# q = []
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == '*':
#             q.append((i,j))
# while q:
#     i, j = q.pop(0)
#     if grid[i+1][j] == '.':
#         grid[i+1][j] = '*'
#         q.append((i+1,j))
#     elif grid[i+1][j] == 'o':
#         if grid[i][j+1] == '.':
#             grid[i][j+1] = '*'
#             q.append((i,j+1))
#         if grid[i][j - 1] == '.':
#             grid[i][j - 1] = '*'
#             q.append((i, j - 1))
# grid = ["".join(i) for i in grid]
# for i in grid:
#     print(i)