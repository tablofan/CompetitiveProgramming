def main():
    for case in range(int(input())):
        n, x, y = map(int, input().split())
        s = ((n+1)*n)//2
        N = list(range(1, n+1))
        N = N[::-1]
        if s%(x+y) != 0:
            print(f'Case #{case + 1}: IMPOSSIBLE')
            continue
        a = (s*x)//(x+y)
        ans = []
        for i in N:
            if i <= a:
                a -= i
                ans.append(i)
        ans.sort()
        print(f'Case #{case + 1}: POSSIBLE')
        print(len(ans))
        print(" ".join([str(i) for i in ans]))



if __name__ == "__main__":
    main()