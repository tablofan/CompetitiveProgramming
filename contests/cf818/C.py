def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    b += [b[0]]
    a += [a[0]]
    for x,y in zip(a,b):
        if x > y:
            return "NO"
    for i in range(len(b)-1):
        if b[i] > b[i+1]+1 and b[i] != a[i]:
            return "NO"
    return "YES"


for _ in range(int(input())):
    print(solve())