def solve():
    inp = [int(i) for i in input().split()]
    t = inp[0]
    res = 0
    for i in inp[1:]:
        if i > t:
            res += 1
    print(res)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
