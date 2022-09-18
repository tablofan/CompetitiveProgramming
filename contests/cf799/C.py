def solve():
    arr = []
    for _ in range(8):
        arr.append(input())

    for i in range(1, 7):
        for j in range(1, 7):
            if arr[i-1][j-1] == '#' and arr[i+1][j+1] == '#' and arr[i-1][j+1] == '#' and arr[i+1][j-1] == '#':
                return f'{i+1} {j+1}'


def main():
    for _ in range(int(input())):
        input()
        print(solve())
    return


if __name__ == "__main__":
    main()
