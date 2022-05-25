
def solve():
    n = input()
    rem = str((9 - sum(int(i) for i in n)%9)%9)
    if rem == '0':
        return n[0] + '0' + n[1:]
    for i,v in enumerate(n):
        if rem < v:
            return n[:i] + rem + n[i:]
    return n + rem


def main():
    for i in range(int(input())):
        print(f'Case #{i+1}: {solve()}')


if __name__=="__main__":
    main()