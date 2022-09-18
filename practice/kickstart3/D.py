import math
def solve(n, s):
    dp = dict()
    def rec(s):
        if len(s) == 1:
            return 2
        if s in dp:
            return dp[s]
        x = 0
        for i in range(len(s)):
            x += rec(s[:i]+s[i+1:])
        if s == s[::-1]:
            x += math.factorial(len(s))
        dp[s] = x
        return x
    total = 0
    for i in range(len(s)):
        total += rec(s[:i] + s[i + 1:])
    gcd = math.gcd(total, math.factorial((len(s))))
    p = total//gcd
    q = math.factorial(len(s))//gcd
    ans = (pow(q, mod - 2, mod)*p)%mod
    return ans


def main():
    for case in range(int(input())):
        n = int(input())
        s = input()
        print(f'Case #{case + 1}: {solve(n, s)}')


if __name__ == "__main__":
    mod = 1000000007
    main()