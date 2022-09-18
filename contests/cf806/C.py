def solve():
    n = int(input())
    lock = [int(i) for i in input().split()]
    res = []
    for i in range(n):
        _, s = input().split()
        res.append((lock[i]+s.count("D")-s.count("U")+10)%10)
    print(*res)
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
