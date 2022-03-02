def recoverArray(nums):
    nums.sort()
    print(nums)
    res = []
    diff = set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            x = abs(nums[i]-nums[j])
            if x%2 == 0 and x:
                diff.add(x//2)
    for x in diff:
        temp = nums.copy()
        for i,v in enumerate(nums):
            if len(res) == len(nums)//2:
                break
            if v - (x*2) in temp:
                res.append(v-x)
                temp[i] = None
                temp[temp.index(v - (x*2))] = None
            elif v + (x*2) in temp:
                res.append(v+x)
                temp[i] = None
                temp[temp.index(v + (x * 2))] = None
            else:
                res = []
                break
    return (res)


def main():
    print(recoverArray([11,6,3,4,8,7,8,7,9,8,9,10,10,2,1,9]))


if __name__ == "__main__":
    main()