from collections import defaultdict
def find():
    n = int(input())
    nums = [int(i) for i in input().split()]
    s = defaultdict(int)
    trapped = 0
    for i,v in nums:
        if v not in s:
            s[v] = i
            trapped += 1
            if ways > 2:
                return "no"
        else:
            s.remove(i)
            ways -= 1
    return "yes"

def main():
    for _ in range(int(input())):
        print(find())
    return

if __name__=="__main__":
    main()
