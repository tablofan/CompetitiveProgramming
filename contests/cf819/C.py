from collections import defaultdict
class ufds:
    parent_node = {}
    rank = {}
    def make_set(self, u):
        for i in u:
            self.parent_node[i] = i
            self.rank[i] = 0

    def op_find(self, k):
        if self.parent_node[k] != k:
            self.parent_node[k] = self.op_find(self.parent_node[k])
        return self.parent_node[k]

    def op_union(self, a, b):
        x = self.op_find(a)
        y = self.op_find(b)

        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent_node[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent_node[x] = y
        else:
            self.parent_node[x] = y
            self.rank[y] = self.rank[y] + 1


def solve():
    input()
    inp = input()
    uf = ufds()
    uf.make_set([i for i in range(1,len(inp)+1)])
    layer = defaultdict(int)
    curr = 0
    for i,v in enumerate(inp):
        if v == "(":
            curr += 1
            if layer[curr]==0:
                layer[curr] = i+1
            else:
                uf.op_union(i+1, layer[curr])
                layer[curr] = i+1
        else:
            layer[curr+1] = 0
            uf.op_union(i+1, layer[curr])
            curr -= 1
    # print(*[uf.parent_node.values()])
    print(len(set(uf.parent_node.values())))
    return


for _ in range(int(input())):
    solve()