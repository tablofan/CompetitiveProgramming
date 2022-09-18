def ctz(v):
    return (v & -v).bit_length() - 1


def solve():
    n = int(input())
    arr = [int(i) for i in input().split()]
    e = [ctz(i) for i in arr if i%2==0]
    o = n - len(e)
    if o:
        return len(e)
    return min(e) + len(e) - 1


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()