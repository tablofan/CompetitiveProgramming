def solve():
    n = int(input())
    a = input()
    b = input()
    a = a.replace("B", "G")
    b = b.replace("B", "G")
    print("YES") if a==b else print("NO")
    return


for _ in range(int(input())):
    solve()