from collections import defaultdict
def bfs(pre,parent):
    depth = [-1 for _ in range(len(pre))]
    d = defaultdict(list)
    for i,v in enumerate(parent):
        depth[i] = depth[v] + 1
        d[depth[v]+1].append(pre[i])
    bfs_order = []
    for i in d.values():
        bfs_order.extend(i)
    return bfs_order


def main():
    pre = [1,2,4,5,3]
    parent = [-1,0,1,1,0]
    print(bfs(pre,parent))

if __name__ == "__main__":
    main()