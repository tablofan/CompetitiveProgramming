from collections import defaultdict
def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    d = defaultdict(list)
    for i,v in enumerate(a):
        d[v].append(i)
    res = len(d.keys())
    # print(res)
    a = a[::-1]
    # print(d)
    for i,v in enumerate(a):
        # print(f'{len(a)-i-1 = }')
        # print(f'{v = }')
        if i!=0 and v > a[i-1]:
            return res
        if i!=len(a)-1 and v == a[i+1]:
            continue
        if d[v][0] < len(a)-i-1:
            return res
        res -= 1
    return res


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()