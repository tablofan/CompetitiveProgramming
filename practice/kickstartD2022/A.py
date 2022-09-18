def median(arr):
    if len(arr)%2==1:
        return arr[len(arr)//2]
    return (arr[len(arr)//2] + arr[(len(arr)//2)-1])/2


def solve():
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    a.sort()
    if n == m:
        return sum(a)
    d = n - m
    res =  median(a[:d+1]) + sum(a[d+1:])
    return res


def main():
    for case in range(int(input())):
        print(f'Case #{case+1}: {solve()}')
    return


if __name__ == "__main__":
    main()
