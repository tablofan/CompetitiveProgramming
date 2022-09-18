from collections import Counter
def solve():
    c = Counter("Timur")
    n = int(input())
    print("YES") if Counter(input()) == c else print("NO")
    return

for _ in range(int(input())):
    solve()