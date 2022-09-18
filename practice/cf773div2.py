#A
# for _ in range(int(input())):
#     a = list(map(int,input().split()))
#     b = list(map(int,input().split()))
#     c = list(map(int,input().split()))
#     if a[1]==b[1] and c[1]<a[1]:
#         print(abs(a[0]-b[0]))
#     elif b[1] == c[1] and a[1]<b[1]:
#         print(abs(b[0]-c[0]))
#     elif a[1]==c[1] and b[1]<a[1]:
#         print(abs(a[0]-c[0]))
#     else:
#         print(0)

#B
# for _ in range(int(input())):
#     n = int(input())
#     powers = [int(i) for i in input().split()]
#     s = set(powers)
#     l = len(s)
#     for i in range(1,n+1):
#         print(max(i,l),end=" ")

#C
# from collections import Counter
# from collections import defaultdict
# for _ in range(int(input())):
#     n, x = map(int,input().split())
#     inp = [int(i) for i in input().split()]
#     c = Counter(inp)
#     d = defaultdict(int,sorted(c.items(),key = lambda i: i[0]))
#     for i in d:
#         if i * x in d:
#             t = min(d[i],d[i*x])
#             d[i]-=t
#             d[i*x]-=t
#     print(sum(d.values()))

#D
from collections import Counter
from collections import deque
for _ in range(int(input())):
    input()
    nums = [int(i) for i in input().split()]
    c = Counter(nums)
    x = True
    for i in c:
        if c[i]&1:
            print(-1)
            x = False
            break
    if x:
        nums = deque(nums)
        res = []
        seen = set()
        curr = []
        r = False
        i = 0
        while nums:
            if r:
                if nums[0]==curr[i]:
                    nums.popleft()
                    i+=1
                    if i == len(curr)-1:
                        res.append(len(curr)*2)
                        curr.clear()
                        i = 0
                        r = False
                else:
                    res.append(len(curr)*2)
                    for j in curr[i:]:
                        nums.appendleft(j)
            elif nums[0] not in seen:
                t = nums.popleft()
                seen.add(t)
                curr.append(t)
            # elif not r:
            #     k = len(curr)
            #     if nums[0]==curr[0]:
