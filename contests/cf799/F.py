from collections import Counter
def solve():
    n = int(input())
    arr = [int(i)%10 for i in input().split()]
    c = Counter(arr)
    # print(c)
    for i in range(10):
        for j in range(i, 10):
            for k in range(j, 10):
                if (i+j+k) % 10 == 3:
                    # print(f'{i = } {j = } {k = }')
                    if i == j == k:
                        if c[i] > 2:
                            return "YES"
                    elif i == j:
                        if c[i] > 1 and c[k] > 0:
                            return "YES"
                    elif j == k:
                        if c[j] > 1 and c[i] > 0:
                            return "YES"
                    elif c[i] > 0 and c[j] > 0 and c[k] > 0:
                        return "YES"
    return "NO"


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
