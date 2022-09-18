def solve():
    n, m = map(int, input().split())
    arr = [int(i) for i in input().split()]
    res = ["B"]*m
    for i in arr:
        a, b = min(i-1, m-i), max(i-1, m-i)
        if res[a] == "B":
            res[a] = "A"
        else:
            res[b] = "A"
    print("".join(res))
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
