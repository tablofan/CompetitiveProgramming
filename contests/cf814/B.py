def solve():
    n, k = map(int, input().split())
    if not k%4:
        print("NO")
        return
    print("YES")
    if k%2:
        for i in range(n//2):
            print(f'{i*2+1} {i*2+2}')
        return
    for i in range(n//2):
        if not i%2:
            print(f'{i*2+2} {i*2+1}')
        else:
            print(f'{i*2+1} {i*2+2}')
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
