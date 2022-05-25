def product(n):
    res = 1
    for i in str(n):
        res *= int(i)
    return res

def solve():
    res = 0
    a, b = map(int, input().split())
    for i in range(a,b+1):
        if product(i) % sum(int(x) for x in str(i)) == 0:
            res += 1
    return res

def main():
    for i in range(int(input())):
        print(f'Case #{i+1}: {solve()}')

if __name__=="__main__":
    main()