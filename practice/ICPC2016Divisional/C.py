#C
n = int(input())
p = [int(i) for i in input().split()]
low = p[0]-1
res = []
for i in p:
    low = min(low+1,i)
    res.append(str(low))
print(" ".join(res))