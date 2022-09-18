def solve():
    pali = {0, 70, 140, 210, 280, 350, 601, 671, 741, 811, 881, 951, 1202, 1272, 1342, 1412}
    c, mins = input().split()
    mins = int(mins)
    c = c.split(":")
    time = int(c[0])*60 + int(c[1])
    res = 0
    if time in pali:
        res += 1
    start = time
    time += mins
    time %= 1440
    while time != start:
        if time in pali:
            res += 1
        time += mins
        time %= 1440
    print(res)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
