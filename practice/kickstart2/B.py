def main():
    for case in range(int(input())):
        n = int(input())
        factors = set()
        res = 0
        for i in range(1,int(n ** 0.5 + 1)):
            if not n%i:
                factors.add(i)
                factors.add(n//i)
        for i in factors:
            if str(i) == str(i)[::-1]:
                res += 1
        print(f'Case #{case+1}: {res}')


if __name__ == "__main__":
    main()