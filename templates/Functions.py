# returns factors of n as set 
# O(sqrt(n))
def factors(n):
    return {f for i in range(1, int(n**0.5)+1) if n % i == 0 for f in [i, n//i]}


# sieve as generator
# O(nlog(log(n)))?
def prime_sieve(limit):
    prime = [True] * limit
    prime[0] = prime[1] = False
    for i, is_prime in enumerate(prime):
        if is_prime:
            yield i
            for n in range(i * i, limit, i):
                prime[n] = False


# uf with path compression
class UnionFind:
    parent_node = {}
    rank = {}
    # Pass through all nodes
    def make_set(self, u):
        for i in u:
            self.parent_node[i] = i
            self.rank[i] = 0

    def find(self, k):
        if self.parent_node[k] != k:
            self.parent_node[k] = self.find(self.parent_node[k])
        return self.parent_node[k]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent_node[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent_node[x] = y
        else:
            self.parent_node[x] = y
            self.rank[y] = self.rank[y] + 1


