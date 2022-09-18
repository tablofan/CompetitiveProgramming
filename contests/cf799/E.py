# from collections import defaultdict
# def solve():
#     n, s = map(int, input().split())
#     cache = set()
#     def rec(start, end, summ, moves):
#         if (start, end) in cache:
#             return 9999999
#         cache.add((start, end))
#         if start > end:
#             return -1
#         if summ == s:
#             return moves
#         if summ < s:
#             return 9999999
#         res = 9999999
#         if arr[start] == 1:
#             res = min(res, rec(start+1, end, summ-1, moves+1))
#         else:
#             res = min(res, rec(start + 1, end, summ, moves + 1))
#         if arr[end] == 1:
#             res = min(res, rec(start, end - 1, summ - 1, moves + 1))
#         else:
#             res = min(res, rec(start, end - 1, summ, moves + 1))
#         return res
#
#     arr = [int(i) for i in input().split()]
#     summm = sum(arr)
#     if summm < s:
#         return -1
#     return rec(0, n-1, summm, 0)
#
#
# def main():
#     for _ in range(int(input())):
#         print(solve())
#     return
#
#
# if __name__ == "__main__":
#     main()

from collections import deque
def peopleAwareOfSecret(n: int, delay: int, forget: int) -> int:
    q = deque([(1, 1)])
    for i in range(1, n + 1):
        while q[0][0] <= i - forget:
            q.popleft()
        curr = 0
        for x in q:
            if x[0] <= i - delay:
                curr += x[1]
        if curr:
            q.append((i, curr))
        print(i)
        print(q)

    res = 0
    for i in q:
        res += i[1]
    return res

print(peopleAwareOfSecret(10,2,5))