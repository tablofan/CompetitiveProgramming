def solve():
    n = int(input())
    s = [int(i) for i in input().split()]
    e = [int(i) for i in input().split()]
    z = set()
    y = set()
    for a, b in zip(s, e):
        if b > a:
            return "NO"
        if b:
            y.add(a-b)
        else:
            z.add(a)
    y = list(y)
    if len(y) > 1:
        return "NO"
    for i in list(z):
        if y and i > y[0]:
            return "NO"
    return "YES"


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
