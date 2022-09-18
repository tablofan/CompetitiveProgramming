from collections import Counter
def solve():
    n = int(input())
    inp = [int(i) for i in input().split()]
    c = Counter(inp)
    for i in c:
        if c[i] == 1:
            print(-1)
            return
    res = []
    count = 0
    for i,v in c.items():
        count += v
        res.append(count)
        for x in range(count - v + 1, count):
            res.append(x)
    print(" ".join([str(i) for i in res]))
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
