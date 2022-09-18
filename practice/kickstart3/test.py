from collections import defaultdict
# from functools import cache

# @cache
def rec(n):
    print(n)
    if n < 1:
        return 0
    if n in dp:
        return dp[n]
    res = rec(n//5) + rec(n//3)
    dp[n] = res
    return res


def main():
    print(rec(47))


if __name__ == "__main__":
    dp = defaultdict(int)
    main()