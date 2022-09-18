from collections import defaultdict

def main():
    n, t = map(int, input().split())
    b = defaultdict(int)
    for _ in range(n):
        p, a = input().split()
        b[p] = int(a)
    for _ in range(t):
        x, y, c = input().split()
        if b[x] < int(c):
            continue
        b[x] -= int(c)
        b[y] += int(c)
    for k,v in sorted(b.items()):
        print(k+" "+str(v))

if __name__=="__main__":
    main()