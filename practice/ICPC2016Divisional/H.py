#H
from functools import cache
def main():
    l, r, t = map(int, input().split())
    t //= 100

    @cache
    def dfs(l, r, t):
        # print(f'l:{l} r:{r} t:{t}')
        if l>r or t<1:
            return 0
        ans = 0
        for i in range(l, r+1):
            accept = max(dfs(i,r,t-2),i)
            reject = dfs(l,i-1,t-1)
            ev = (accept*(r-i+1)+reject*(i-l))/(r-l+1)
            ans = max(ans, ev)
        return ans
    return dfs(l,r,t)


if __name__ == "__main__":
    print(main())