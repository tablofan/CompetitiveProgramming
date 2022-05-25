
from collections import defaultdict

def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2]


def main():
    n, m, dist = map(int, input().split())
    s = 0
    d = defaultdict(list)

    for _ in range(m):
        a, b, t = map(int, input().split())
        s += b
        d[t].append(a)
    medhigh = 0
    medlow = 0
    pos = 0
    lastk = 0
    for k,v in sorted(d.items()):
        pos =

if __name__=="__main__":
    main()