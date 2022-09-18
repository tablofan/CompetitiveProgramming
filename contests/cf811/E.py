def solve():
    int(input())
    a = list(set(int(i)+int(i)%10 if int(i)%2 else int(i) for i in input().split()))
    a.sort()
    curr = a[0]
    for i,v in enumerate(a[1:]):
        if not curr % 10 and curr != v:
            return "No"
        curr += ((v-curr)//20)*20
        while curr < v:
            curr += curr%10
        if curr > v:
            return "No"
    return "Yes"


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
