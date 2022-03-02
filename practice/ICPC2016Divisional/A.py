# A
k = list(map(int,input().split()))[1]
n = [int(i) for i in input().split()]
res = 0
rem = 0
for i in n:

    if i<=rem:
        rem -= i
    else:
        res += (i//k)
        if i%k:
            res += 1
        rem = (k - i%k)%k
print(res)