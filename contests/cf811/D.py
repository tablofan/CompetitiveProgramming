def main():
    length = int(input())
    for _ in range(length):
        base = input()
        n = int(input())
        arr = []
        for _ in range(n):
            candidate = input()
            arr.append(candidate)

        res, lst = solver(base, arr)
        print(res)
        for num1, num2 in lst:
            print(str(num1) + " " + str(num2))


def solver(base, arr):
    n = len(base)
    dp = [float("inf") for _ in range(len(base) + 1)]
    _from = [[0, 0] for _ in range(len(base) + 1)]
    dp[0] = 0
    for right in range(1, n + 1):
        for left in range(right):
            word = base[left: right]
            if word not in arr:
                continue
            ind = arr.index(word)
            no_used = dp[left] + 1
            if no_used < dp[right]:
                for j in range(left + 1, right + 1):
                    if no_used < dp[j]:
                        dp[j] = min(dp[j], no_used)
                        _from[j][0] = left + 1
                        _from[j][1] = ind + 1
    res = dp[-1] if dp[-1] != float("inf") else -1
    lst = []
    if res != -1:
        i = len(base)
        while i > 0:
            lst.append((_from[i][1], _from[i][0]))
            i = _from[i][0] - 1
    return res, lst


if __name__ == "__main__":
    main()