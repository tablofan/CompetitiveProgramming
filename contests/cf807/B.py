def solve():
    n = int(input())
    room = [int(i) for i in input().split()]
    res = 0
    i = 0
    while not room[i] and i < n-1:
        i += 1
    res += room[i:-1].count(0)
    res += sum(room[i:-1])
    print(res)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
