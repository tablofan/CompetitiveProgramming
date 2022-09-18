def solve():
    n, k = map(int, input().split())
    s = input()
    res = s[:k].count('W')
    # print(f'{s[:k] = }')
    curr = res
    for i in range(n - k):
        # print(f'{curr = }')
        if s[i+k] == 'W':
            curr += 1
        if s[i] == 'W':
            curr -= 1
        res = min(res, curr)
    return res


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
