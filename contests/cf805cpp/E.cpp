from collections import defaultdict
class UF:
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.size = {i: 1 for i in range(n)}

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return

        if self.size[rootX] <= self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
            self.size[rootX] = 0

        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            self.size[rootY] = 0

def solve():
    dominos = int(input())
    uf = UF(dominos)
    l = defaultdict(int)
    for _ in range(dominos):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        l[a] += 1
        l[b] += 1
        uf.union(a, b)
    if all(i == 2 for i in l.values()) and all(i%2==0 for i in uf.size.values()):
        print("YES")
    else:
        print("NO")


    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
