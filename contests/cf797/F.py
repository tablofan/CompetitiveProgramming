class UF:
    parent_node = {}

    def make_set(self, u):
        for i in u:
            self.parent_node[i] = i

    def find(self, k):
        if self.parent_node[k] == k:
            return k
        return self.find(self.parent_node[k])

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        self.parent_node[x] = y


def display(u, uf):
    print([uf.find(i) for i in u])


def solve():
    uf = UF()
    n = int(input())
    s = list(input())
    p = [int(i)-1 for i in input().split()]
    uf.make_set(p)
    for i,v in enumerate(p):
        uf.union(i, v)
    display(p, uf)


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
