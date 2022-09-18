def solve():
    n = int(input())
    res = 4 * (n // 3) if n//3 else 0
    res += ((n//2-n//3)*2) if n//2 else 0
    res += n
    print(res)
    return


for _ in range(int(input())):
    solve()