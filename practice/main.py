#A
# def solve(n,l):
#     counts = [0 for i in range(l)]
#     arr = [bin(int(x))[2:] for x in input().split()]
#     for i in arr:
#         for ind,v in enumerate(i[::-1]):
#             counts[ind]+=1 if v=='1' else 0
#     y = ""
#     for i in counts[::-1]:
#         y+="1" if i > n//2 else "0"
#     print(int(y,2))
#
#
# def main():
#     for _ in range(int(input())):
#         n, l = map(int, input().split())
#         solve(n, l)
#
#
# if __name__ == "__main__":
#     main()

#B
def solve(n,l):
    counts = [0 for i in range(l)]
    arr = [bin(int(x))[2:] for x in input().split()]
    for i in arr:
        for ind,v in enumerate(i[::-1]):
            counts[ind]+=1 if v=='1' else 0
    y = ""
    for i in counts[::-1]:
        y+="1" if i > n//2 else "0"
    print(int(y,2))


def main():
    for _ in range(int(input())):
        n, l = map(int, input().split())
        solve(n, l)


if __name__ == "__main__":
    main()