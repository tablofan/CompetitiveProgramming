#D
n, h, v, w = map(int, input().split())
nearest = 1 << (h - 1).bit_length()
tree = [0 for _ in range(2 * nearest)]


def update(node,nodelow, nodehigh, updatelow, updatehigh):
    if updatelow <= nodelow and updatehigh >= nodehigh:
        tree[node] = 1
        return
    if nodehigh < updatelow or nodelow > updatehigh:
        return
    lastinleft = (nodelow + nodehigh)//2
    update(2*node, nodelow, lastinleft, updatelow, updatehigh)
    update(2*node+1, lastinleft+1, nodehigh, updatelow, updatehigh)
    return


def query(root):
    if tree[root]:
        return True
    if root>nearest:
        return False
    return query(2*root) and query(2*root+1)


if v*w >= h:
    print("GAME OVER")
else:
    update(1, 0, nearest-1, h,nearest-1)
    for _ in range(n):
        c,r = map(int,input().split())
        start = (r + c*v)%h
        end = (start+w*v)%h
        if start > end:
            update(1, 0, nearest-1,start, h-1)
            update(1, 0, nearest-1, 0, end)
        else:
            update(1, 0, nearest-1, start, end)
    print("GAME OVER") if query(1) else print("VICTORY")