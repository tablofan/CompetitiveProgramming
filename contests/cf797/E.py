from collections import deque
def solve():
    n, k = map(int, input().split())
    inp = [int(i) for i in input().split()]
    res = 0
    for i,v in enumerate(inp):
        res += v//k
        inp[i] %= k
    inp.sort(reverse=True)
    # print(f'{res = }')
    q = deque(inp)
    # print(q)
    while q:
        a = q.popleft()
        while q:
            b = q.pop()
            if a+b >= k:
                res += 1
                break
    return res


def main():
    for _ in range(int(input())):
        print(solve())
    return


if __name__ == "__main__":
    main()
