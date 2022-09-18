def solve():
    s = input()
    cmin = cmax = 0
    v = 0
    for i in s:
        if i == "(":
            cmax += 1
            cmin += 1
        if i == ")":
            cmax -= 1
            cmin = max(cmin-1, 0)
        if i == "?":
            cmax += 1
            
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
