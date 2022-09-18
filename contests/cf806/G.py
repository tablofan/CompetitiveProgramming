def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    vs = []
    prefs = [0] * (n + 1)
    for i in range(n):
        prefs[i + 1] = prefs[i] + a[i]
    ans = sum(a) - k * n
    for i in range(n - 1, -1, -1):
        vs = [(x >> 1) for x in vs if x > 1]
        vs.append(a[i] >> 1)
        nv = prefs[i] + sum(vs) - k * i
        if nv > ans:
            ans = nv
    print(ans)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()