from collections import defaultdict
def solve():
    n = int(input())
    d = defaultdict(list)
    for ind,v in enumerate([int(i) for i in input().split()]):
        d[v].append(ind)
    res = [0 for _ in range(n+1)]
    for key in range(1, n+1):
        if key not in d:
            continue
        curr = d[key][0]
        res[key] += 1
        for i in d[key][1:]:
            if (i - curr) % 2:
                res[key] += 1
                curr = i
    print(*res[1:])
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
