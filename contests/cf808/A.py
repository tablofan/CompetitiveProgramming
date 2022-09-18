def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in a[1:]:
        if i%a[0]:
            return "NO"
    return "YES"


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()