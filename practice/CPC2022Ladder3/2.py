def solve():
    n = int(input())
    nums = sorted([int(i) for i in input().split()])
    return nums[-1] + nums[-2]


def main():
    for i in range(int(input())):
        print(solve())


if __name__ == "__main__":
    main()