def solve():
    n = int(input())
    base = n//3
    rem = n%3
    # print(f'{n = }')
    if not rem:
        print(str(base) + " " + str(base+1) + " " + str(base-1))
    elif rem == 1:
        print(str(base) + " " + str(base+2) + " " + str(base-1))
    else:
        print(str(base+1) + " " + str(base+2) + " " + str(base-1))
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()