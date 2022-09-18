def ctz(v):
    return (v & -v).bit_length() - 1

def solve():
    n = int(input())
    if n == 1 or n == 2:
        return 3
    z = ctz(n)
    b = bin(n)
    ones = sum(1 for i in b if i == '1')
    # print(f'{n = }')
    # print(f'{z = }')
    # print(f'{b = }')
    # print(f'{ones = }')
    if ones > 1:
        return 2**z
    return n + 1



def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()

t = 2
arr = [1, 2, 3, 4, 1]