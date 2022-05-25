from collections import Counter


def main():
    def solve(val):
        if c[val] > 0:
            c[val] -= 1
            return True
        if val == 1:
            return False
        return solve(val//2) and solve((val+1)//2)
    for _ in range(int(input())):
        input()
        inp = [int(i) for i in input().split()]
        c = Counter(inp)
        print("Yes" if solve(sum(inp)) else "NO")


if __name__ == "__main__":
    main()

