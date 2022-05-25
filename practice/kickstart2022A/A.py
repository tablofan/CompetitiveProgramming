def solve():
    res = 0
    a = input()
    b = input()
    j = 0
    for i in range(len(a)):
        if j>=len(b):
            return 'IMPOSSIBLE'
        while a[i] != b[j]:
            j += 1
            if j>=len(b):
                return 'IMPOSSIBLE'
            res += 1
        j += 1
    return res + len(b) - j


def main():
    for i in range(int(input())):
        print(f'Case #{i+1}: {str(solve())}')


if __name__=="__main__":
    main()