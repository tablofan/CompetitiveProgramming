def solve():
    n, q = map(int, input().split())
    t = [int(i) for i in input().split()]
    if q >= n:
        return "1"*n
    t = t[::-1]
    iq = 1
    i = 0
    res = ""
    while i < len(t)-1:
        i += 1
        if iq > q:
            break
        if iq < t[i]:
            iq += 1

    if i > 1:
        res += "1" * (i-1)
    # print(t)
    # print(f'{res = } {iq = } {i = }')
    # print(t[i-1:])
    for x in t[i-1:]:
        if q < x:
            res += "0"
        else:
            res += "1"
    res = "1" + res[1:]
    return res[::-1]


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
