from collections import defaultdict
def kadane(l):
    maxsofar = 1
    curr = 1
    end = l[0]
    start = l[0]
    currstart = l[0]
    for i,v in enumerate(l[1:]):
        curr += l[i] - v + 2
        if curr > maxsofar:
            maxsofar = curr
            start = currstart
            end = v
        if curr < 1:
            curr = 1
            currstart = v
        # print(f'{curr = }')
        # print(f'{start = }')
        # print(f'{end = }')
    return ((maxsofar, start, end))

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    d = defaultdict(list)
    for i,v in enumerate(a):
        d[v].append(i)
    # print(f'{d = }')
    res = (1, 0, 0)
    reskey = a[0]
    for key in d:
        ans = kadane(d[key])
        if ans[0] > res[0]:
            res = ans
            reskey = key
    # print(f'{res = }')
    # print(f'{reskey = }')

    print(f'{reskey} {res[1]+1} {res[2]+1}')
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
