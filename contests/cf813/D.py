def solve():
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    
    a.sort()
    for i in range(k):
        a[i] = 1000000000
    a.sort()
    if n == 2:
        return a[0]
    return min(a[-2], 2*a[0])


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()