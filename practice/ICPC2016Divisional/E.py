#E
n, t = map(int,input().split())
n -= 2
dp = [0 for _ in range(-(-(n)//2-1)-1)]
for i in range(1,len(dp)):
    dp[i] = dp[i-1]+(n-len(dp)-i+1)*9*(10**(i-1))
if t>dp[-1]:
    print(-1)
else:
    for i,v in enumerate(dp):
        if t<=v:
            d = i
            break
    temp = n
    while len(dp)>2:
        temp -= 2
        dp = [0 for _ in range(-(-(temp) // 2 - 1) - 1)]
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + (n - len(dp) - i + 1) * 9 * (10 ** (i - 1))
        for i, v in enumerate(dp):
            if t <= v:
                d = min(d,i)
                break
    dp = [0 for _ in range(d)]
    for i in range(1, d):
        dp[i] = dp[i-1]+(n-d-i)*9*(10**(i-1))
    res = -(-(t-dp[-1])//(n-d*2))
    res += int("9"*(d-1)) if d>1 else 0
    print(res)