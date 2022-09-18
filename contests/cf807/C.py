def solve():
    n, c, queries = map(int, input().split())
    o = input()
    copies = []
    l = len(o)
    for _ in range(c):
        a, b = map(int, input().split())
        copies.append((l+1, l+b-a+1, a, b))
        l += b - a + 1
    print(copies)
    for _ in range(queries):
        q = int(input())
        if q <= len(o):
            print(o[q-1])
            continue
        ind = 0
        for i,v in enumerate(copies):
            if v[0] <= q <= v[1]:
                ind = i
                break
        while ind > -1 and q > len(o):

            q = copies[ind][2] + q - copies[ind][0]
            print(f'{ind = } {q = }')
            ind -= 1
            while ind > -1 and q > copies[ind][1]:
                ind -= 1
        print(o[q-1])
    return



def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()