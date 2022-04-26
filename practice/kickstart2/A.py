import math
def main():
    for n in range(int(input())):
        pi = math.pi
        r, a, b = map(int, input().split())
        curr = r * a
        s = r*r*pi + curr*curr*pi
        curr //= b
        s += curr*curr*pi
        while curr > 0:
            curr *= a
            s += curr*curr*pi
            curr //= b
            s += curr*curr*pi
        print(f'Case #{n+1}: {s}')


if __name__ == "__main__":
    main()