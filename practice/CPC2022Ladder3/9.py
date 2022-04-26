def main():
    _, r = map(int, input().split())
    a = [int(i) for i in input().split()]
    balls = []
    for i in a:
        pos = r
        for x, y in balls:
            if abs(x-i) <= 2*r:
                pos = max(pos, ((4*r*r - (x-i)**2)**0.5)+y)
        balls.append([i, pos])
        print(pos, end=" ")


if __name__ == "__main__":
    main()
