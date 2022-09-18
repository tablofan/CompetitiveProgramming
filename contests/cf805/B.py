def solve():
    n = input()
    res = 0
    s = set()
    for i in n:
        if i in s:
            continue
        if len(s) == 3:
            s.clear()
            res += 1
        s.add(i)
    print(res+1)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
