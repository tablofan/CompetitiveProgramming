def solve():
    n = int(input())
    curr = 9
    res = []
    while n > curr:
        res.append(curr)
        n -= curr
        curr -= 1
    if n:
        res.append(n)
    print("".join(str(i) for i in res[::-1]))
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
