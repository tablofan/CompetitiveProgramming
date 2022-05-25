def solver(i, a, b):
    global res
    # print(f'{a = }')
    # print(f'{b = }')
    if res >= best or a > best or b> best:
        return
    if a == b:
        res = max(a, res)
    # print(f'{res = }')
    if i == n:
        return
    solver(i + 1, a + nums[i], b)
    solver(i + 1, a, b + nums[i])
    solver(i + 1, a, b)
    return


def main():
    solver(0, 0, 0)


if __name__ == "__main__":
    n = int(input())
    nums = [int(i) for i in input().split()]
    best = sum(nums) / 2
    res = 0
    main()
    print(res)
