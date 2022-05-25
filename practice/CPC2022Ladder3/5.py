def up(curr):
    seg[curr] = seg[curr << 1] + seg[curr << 1 | 1]
    return


def down(curr, length):
    if lazy[curr]:
        lazy[curr << 1] ^= 1
        lazy[curr << 1 | 1] ^= 1
        seg[curr << 1] = length - (length >> 1) - seg[curr << 1]
        seg[curr << 1 | 1] = (length >> 1) - seg[curr << 1 | 1]
        lazy[curr] = 0
    return


def update(start, end, l, r, curr):
    if start <= l and end >= r:
        seg[curr] = r - l + 1 - seg[curr]
        lazy[curr] ^= 1
        return
    down(curr, r - l + 1)
    mid = (l + r) // 2
    if start <= mid:
        update(start, end, l, mid, curr << 1)
    if end > mid:
        update(start, end, mid+1, r, curr << 1 | 1)
    up(curr)
    return


def query(start, end, l, r, curr):
    if start <= l and end >= r:
        return seg[curr]
    down(curr, r - l + 1)
    mid = (l + r) // 2
    res = 0
    if start <= mid:
        res += query(start, end, l, mid, curr << 1)
    if end > mid:
        res += query(start, end, mid+1, r, curr << 1 | 1)
    return res


def main():
    n, m = map(int, input().split())
    for _ in range(m):
        t, start, end = map(int, input().split())
        if not t:
            update(start, end, 1, n, 1)
        else:
            print(query(start, end, 1, n, 1))


if __name__ == "__main__":
    N = 100005
    a = [0] * N
    seg = [0] * (3 * N)
    lazy = [0] * (3 * N)
    main()
