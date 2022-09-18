from collections import defaultdict

def main():
    length = int(input())

    for _ in range(length):
        input()
        n, l = list(map(int, input().split(" ")))
        arr = list(map(int, input().split(" ")))
        letter_mapping = defaultdict(list)
        for i in range(n):
            letter_mapping[arr[i]].append(i)

        for _ in range(l):
            _from, _to = list(map(int, input().split(" ")))
            ans = solver(_from, _to, letter_mapping)
            print(ans)


def solver(_from, _to, mapping):
    if _from not in mapping or _to not in mapping:
        return "NO"

    lst1 = mapping[_from]
    lst2 = mapping[_to]

    p1, p2 = 0, 0

    while p1 < len(lst1) and p2 < len(lst2):
        if lst1[p1] < lst2[p2]:
            return "YES"
        p2 += 1

    return "NO"


main()