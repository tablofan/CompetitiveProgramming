from collections import deque
def main():
    for case in range(int(input())):
        ants, stick = map(int, input().split())
        a = []
        order = []
        for i in range(1, ants+1):
            n, direct = map(int, input().split())
            if direct:
                dist = stick - n
            else:
                dist = n
            order.append((n, i))
            a.append((dist, direct))
        order.sort()
        d = deque(order)
        a.sort()
        # print(f'{order = }')
        # print(f'{a = }')
        ans = []
        a = a[::-1]
        while a:
            dist, direct = a.pop()
            if a and dist == a[-1][0]:
                a.pop()
                xx = d.pop()[1]
                yy = d.popleft()[1]
                ans.append(min(xx, yy))
                ans.append(max(xx, yy))
            else:
                if direct:
                    ans.append(d.pop()[1])
                else:
                    ans.append(d.popleft()[1])
        print(f'Case #{case + 1}: {" ".join([str(i) for i in ans])}')



if __name__ == "__main__":
    main()