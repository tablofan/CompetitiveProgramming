import heapq
def solve():
    n = int(input())
    nums = [int(i) for i in input().split()]
    heapq.heapify(nums)
    while len(nums) > 1:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        if b-a > 1:
            return "No"
        heapq.heappush(nums,a+b)
    return "Yes"

def main():
    for _ in range(int(input())):
        print(solve())


if __name__=="__main__":
    main()