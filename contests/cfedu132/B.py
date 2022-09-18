def accumulate(x, l=[0]): l[0] += x; return l[0];
def solve():
    n, m = map(int, input().split())
    h = [int(i) for i in input().split()]
    inc = [max(0, h[i]-v) for i,v in enumerate(h[1:])]
    dec = [max(0, v-h[i]) for i,v in enumerate(h[1:])]
    curr = 0
    forw = [0]
    back = [0]
    for i in inc:
        curr += i
        forw.append(curr)
    curr = 0
    for i in dec:
        curr += i
        back.append(curr)
    # print(forw)
    # print(back)
    for _ in range(m):
        a, b = map(int, input().split())
        if a < b:
            print(forw[b-1] - forw[a-1])
        else:
            print(back[a-1] - back[b-1])
    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()
