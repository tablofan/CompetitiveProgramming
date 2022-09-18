import bisect
def solve():
    n = int(input())
    inp = [int(i) for i in input().split()]
    i = []
    j = []
    res = 0
    for ind,val in enumerate(inp):
        if ind+1 > val:
            i.append(ind+1)
            j.append(val)
    j.sort()
    for x in i:
        res += len(j) - bisect.bisect_right(j, x)
    print(res)

    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
