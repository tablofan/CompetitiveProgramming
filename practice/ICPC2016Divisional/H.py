#H
from functools import cache


def main():
    l, r, t = map(int, input().split())
    t //= 100
    # if (r-l)<t:
    #     return (r+l)/2


    print(t)
    @cache
    def dfs(l, r, curr, t):
        print(f'l:{l} r:{r} curr:{curr} t:{t}')
        if not t:
            return (r - curr + 1) * curr
        m = 0
        for i in range(l, curr):
            m = max(m, dfs(l, curr - 1, i, t - 1))
        return (r - curr + 1) * curr + m

    m = 0
    for i in range(l,r+1):
        m = max(m, dfs(l,r,i,t-1))
    print(m)
    return m/(r-l+1)

if __name__ == "__main__":
    print(main())