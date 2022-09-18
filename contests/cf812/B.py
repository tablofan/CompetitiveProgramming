def solve():
    n = int(input())
    a = [0] + [int(i) for i in input().split()] + [0]
    p = 0
    up = True
    for i in range(1, n+2):
        if a[i] == a[i-1]:
            continue
        if a[i] > a[i-1]:
            up = True
        elif up:
            up = False
            p += 1
            if p > 1:
                return "NO"
    return "YES"


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()