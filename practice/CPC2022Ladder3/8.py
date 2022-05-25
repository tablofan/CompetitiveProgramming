import heapq
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.nodes = set(range(n))
        self.edges = defaultdict(list)
        self.dist = defaultdict(int)

    def add_edge(self, a, b, d):
        self.edges[a].append(b)
        self.edges[b].append(a)
        self.dist[(a, b)] = d
        self.dist[(b, a)] = d


def djikstra(g, start, end):
    visited = {start: 0}
    h = [(0, start)]
    nodes = set(g.nodes)
    while nodes and h:
        weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                weight, min_node = heapq.heappop(h)
        except IndexError:
            break
        nodes.remove(min_node)
        for v in g.edges[min_node]:
            w = weight + g.dist[min_node, v]
            if v not in visited or w < visited[v]:
                visited[v] = w
                heapq.heappush(h, (w, v))
    if end in visited:
        return visited[end]
    return 'unreachable'


def main():
    for case in range(int(input())):
        n, m, start, end = map(int, input().split())
        g = Graph(n)
        for _ in range(m):
            a, b, d = map(int, input().split())
            g.add_edge(a, b, d)
        print("Case #"+str(case+1)+": "+ str(djikstra(g, start, end)))


if __name__ == "__main__":
    main()
