# L
from collections import defaultdict, deque
groups = []
d = defaultdict(int)


def dfs(l,r,i):
    if (l,r,i) in d:
        return d[(l,r,i)]
    if l<0 or r<0:
        return -1
    if i==len(groups):
        return r+l
    left = dfs(l - groups[i][0], r - groups[i][1], i + 1)
    d[(l - groups[i][0], r - groups[i][1], i + 1)] = left
    right = dfs(l-groups[i][1],r-groups[i][0],i+1)
    d[(l-groups[i][1],r-groups[i][0],i+1)] = right
    return max(left,right)


def main():
    l,r,n,c = map(int,input().split())
    graph = []
    for _ in range(c):
        graph.append(sorted([int(i) for i in input().split()]))
    graph.sort(key=lambda x:[x[0],x[1]])
    adj = dict()
    for i in range(n):
        adj[i] = []
    for a,b in graph:
        adj[a].append(b)
        adj[b].append(a)
    v = [0 for _ in range(n)]
    lq = deque()
    rq = deque()
    free = 0
    for i in range(n):
        if not v[i]:
            left = 1
            right = 0
            lq.append(i)
            v[i] = 1
            while lq or rq:
                for curr in lq:
                    for j in adj[curr]:
                        if v[curr] == v[j]:
                            return "No"
                        if not v[j]:
                            # print(f"curr:{curr} j:{j} v[j]:{v[j]} left:{left} right:{right}")
                            rq.append(j)
                            right += 1
                            v[j] = 2
                lq.clear()
                for curr in rq:
                    v[curr] = 2
                    for j in adj[curr]:
                        if v[curr] == v[j]:
                            return "No"
                        if not v[j]:
                            # print(f"curr:{curr} j:{j} v[j]:{v[j]} left:{left} right:{right}")
                            lq.append(j)
                            left += 1
                            v[j] = 1
                rq.clear()
            if left == 1 and right == 0:
                free += 1
            else:
                groups.append((left,right))
    # print(v)
    # print(groups)
    return "Yes" if dfs(l,r,0)>=free else "No"


if __name__=="__main__":
    print(main())