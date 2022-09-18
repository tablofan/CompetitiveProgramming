from collections import Counter
length = int(input())

for _ in range(length):
    no_elements = int(input())
    nums = list(map(int, input().split(" ")))
    counter = Counter(nums)
    res = len(counter)
    no_odd = 0

    for key, val in counter.items():
        if (val - 1) % 2 == 1:
            no_odd += 1
    res = res if no_odd % 2 == 0 else res - 1
    print(res)