# I
class suffix:
    def __init__(self):
        self.index = 0
        self.rank = [0, 0]


def buildSuffix(txt, n):
    s = [suffix() for _ in range(n)]
    for i in range(n):
        s[i].index = i
        s[i].rank[0] = (ord(txt[i]) - ord("A"))
        s[i].rank[1] = (ord(txt[i + 1]) - ord("A")) if ((i + 1) < n) else -1
    s = sorted(s, key=lambda x: (x.rank[0], x.rank[1]))
    ind = [0] * n
    k = 4
    while k < 2 * n:
        rank = 0
        prev_rank = s[0].rank[0]
        s[0].rank[0] = rank
        ind[s[0].index] = 0
        for i in range(1, n):
            if s[i].rank[0] == prev_rank and s[i].rank[1] == s[i - 1].rank[1]:
                prev_rank = s[i].rank[0]
                s[i].rank[0] = rank
            else:
                prev_rank = s[i].rank[0]
                rank += 1
                s[i].rank[0] = rank
            ind[s[i].index] = i
        for i in range(n):
            nextindex = s[i].index + k // 2
            s[i].rank[1] = s[ind[nextindex]].rank[0] \
                if (nextindex < n) else -1
        s = sorted(s, key=lambda x: (x.rank[0], x.rank[1]))
        k *= 2
    res = [0] * n
    for i in range(n):
        res[i] = s[i].index
    return res


def buildLCP(t, suf):
    n = len(suf)
    inv = [0 for _ in range(n)]
    for i in range(n):
        inv[suf[i]] = i
    lcp = [0 for _ in range(n)]
    k = 0
    for i in range(n):
        if inv[i] == n - 1:
            k = 0
            continue
        j = suf[inv[i] + 1]
        while i + k < n and j + k < n and t[i + k] == t[j + k]:
            k += 1
        lcp[inv[i]] = k
        if k > 0:
            k -= 1
    return lcp


def main():
    s1 = input()
    s2 = input()
    t = s1 + "#" + s2 + "$"
    len1 = len(s1)
    suf = buildSuffix(t, len(t))
    print(suf)
    lcp = buildLCP(t, suf)
    print(lcp)
    q = []
    for i in range(2, len(lcp) - 1):
        if suf[i] > len1 > suf[i + 1] or suf[i] < len1 < suf[i + 1]:
            q.append((max(suf[i], suf[i + 1]),lcp[i]))
    q = sorted([(a-len1-1, b) for a, b in q if b])
    print(q)
    v = [0 for _ in range(len(s2) + 1)]
    res = len(s2)
    for a, b in q:
        if not v[b] and not v[b + a]:
            for i in range(a):
                v[b + i] = 1
            res -= (a - 1)
    return res


if __name__ == "__main__":
    print(main())
