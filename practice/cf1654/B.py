from collections import defaultdict
def solve():
    s = input()
    d = defaultdict(set)
    for i,v in enumerate(s):
        d[v].add(i)
    for i,v in enumerate(s):
        d[v].remove(i)
        if not d[v]:
            return s[i:]

def main():
    for _ in range(int(input())):
        print(solve())


if __name__=="__main__":
    main()