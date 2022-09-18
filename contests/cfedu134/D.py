from collections import defaultdict
class Trie:
    def __init__(self):
        self.root = {}

    def __bool__(self):
        return bool(self.root)

    def insert(self, num):
        node = self.root
        for x in bin(num)[2:].zfill(32):
            node = node.setdefault(int(x), {})
        node["#"] = num

    def query(self, num):
        node = self.root
        for x in bin(num)[2:].zfill(32):
            node = node.get(1 - int(x)) or node.get(int(x))
        temp = node["#"]
        del node["#"]
        return num ^ temp



def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    trie = Trie()
    for i in b:
        trie.insert(i)
    for i in a:
        print(i)
        print(trie.query(i))
    return


for _ in range(int(input())):
    solve()