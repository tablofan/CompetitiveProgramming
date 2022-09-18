def solve():
    n, h, m = map(int, input().split())
    clocks = []
    for _ in range(n):
        clocks.append(map(int, input().split()))
    clocks = [[a-h, b-m] for a,b in clocks]
    for i,v in enumerate(clocks):
        if v[1] < 0:
            v[1] += 60
            v[0] -= 1
        if v[0] < 0:
            v[0] += 24
    print(*min(clocks))
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()