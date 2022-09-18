from collections import Counter
def solve():
    a = sorted(list(Counter(input() + input()).values()))
    if a == [2, 2]:
        print(1)
    if a == [1, 1, 2]:
        print(2)
    if a == [4]:
        print(0)
    if a == [1, 3]:
        print(1)
    if a == [1, 1, 1, 1]:
        print(3)

    return


for _ in range(int(input())):
    solve()
