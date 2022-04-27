import math


def main():
    def update(start, end, l, r, curr):
        if start <= l and end >= r:
            seg[curr] += 1
            return
        mid = (l + r) // 2
        if start <= mid:
            update(start, end, l, mid, curr << 1)
        if end > mid:
            update(start, end, mid + 1, r, curr << 1 | 1)
        return
    for _ in range(int(input())):
        n = int(input())
        p = 2**(math.ceil(math.log(n)/math.log(2)))
        inp = list(map(int, input().split()))
        seg = [0 for _ in range(p)] + [i-v+1 for i, v in enumerate(inp)] + [0 for _ in range(p-n)]
        for i, v in enumerate(inp):
            if v:
                update(i-v, i-1, 0, p-1, 1)
        for i in range(1, p):
            seg[i << 1] += seg[i]
            seg[i << 1 | 1] += seg[i]
        for i in range(n-1):
            print(seg[p+i], end=" ")
        print(seg[p+n-1])


if __name__ == "__main__":
    main()
