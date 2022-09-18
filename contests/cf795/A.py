def solve():
    input()
    x = [int(i) for i in input().split()]
    o = sum(1 for i in x if i%2==1)
    e = sum(1 for i in x if i%2==0)
    return min(o, e)


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
