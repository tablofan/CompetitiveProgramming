def solve():
    n, k = map(int, input().split())
    inp = input()
    ones = inp.count('1')
    if ones == 0:
        return 0
    front = inp.find('1')
    end = inp[::-1].find('1')
    # print(f'{front = }')
    # print(f'{end = }')
    if ones == 1:
        if k >= end:
            return 1
        if k >= front:
            return 10
        return 11
    inp = list(inp)
    # print(f'{inp = }')
    if k >= end != 0:
        k -= end
        inp[len(inp)-end-1] = '0'
        inp[-1] = '1'
    # print(f'{inp = }')
    if k >= front != 0:
        inp[0] = '1'
        inp[front] = '0'
    # print(f'{inp = }')
    res = 0
    for i in range(len(inp)-1):
        res += int(inp[i]+inp[i+1])

    return res


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
