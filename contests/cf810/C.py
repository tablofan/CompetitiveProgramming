from collections import deque
def check(n, m, k):
    # print(f'{n = }')
    # print(f'{m = }')
    cols = n
    odd = False
    for i in k:
        # print(f'{i = }')
        # print(f'{cols = }')
        temp = i//m
        if temp < 2:
            return False
        if temp > 2:
            odd = True
        # print(f'{temp = }')
        cols -= temp
        if cols == 1 and not odd:
            return False
        if cols == 1 and odd:
            cols += 1
        if cols <= 0:
            return True
    return False



def solve():
    n, m, kk = map(int, input().split())
    k = [int(i) for i in input().split()]
    k.sort(reverse=True)
    if check(n, m, k[:]) or check(m, n, k):
        print("Yes")
    else:
        print("No")
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
