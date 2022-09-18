def solve():
    n = int(input())
    arr = [int(i) for i in input().split()]
    a = 0
    diff = []
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            diff.append(0)
        else:
            diff.append(max(arr[i - 1] - arr[i], arr[i + 1] - arr[i]) + 1)
    print(*diff)
    # if n%2:
    #     print(sum(diff[::2]))
    # else:
    #     s = sum(diff)
    #     pre = []
    #     suf = []
    #     for i in

    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
