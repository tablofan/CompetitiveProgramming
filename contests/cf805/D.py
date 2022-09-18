from collections import defaultdict
def solve():
    alpha = " abcdefghijklmnopqrstuvwxyz"
    s = [ord(i)-96 for i in input()]
    p = int(input())
    d = defaultdict(list)
    for i,v in enumerate(s):
        d[v].append(i)
    deleted = set()
    cost = sum(k*len(v) for k,v in d.items())
    # print(cost)
    while cost > p:
        deleted.add(d[max(d)].pop())
        cost -= max(d)
        # print(d)
        if not len(d[max(d)]):
            del d[max(d)]
    res = [alpha[v] for i,v in enumerate(s) if i not in deleted]
    print("".join(res))
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
