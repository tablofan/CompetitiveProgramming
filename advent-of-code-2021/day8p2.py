from itertools import *

def main():
    with open("input.txt") as file:
        A = [line.strip().split(' | ') for line in file]
    ans2 = 0
    N = len(A)
    ct = [0 for _ in range(10)]
    for i in range(N):
        a = A[i][1]
        for x in a.split():
            ct[len(x)] += 1
    nums = ["abcefg","cf","acdeg","acdfg","bcdf","abdfg","abdefg","acf","abcdefg","abcdfg"]
    valid = set([num.upper() for num in nums])
    for i in range(N):
        done = False
        for perm in permutations("abcdefg".upper()):
            val = ok(A[i][0], A[i][1], perm, valid, nums)
            if val >= 0:
                assert done is False
                ans2 += val
                done = True
        assert done is True
    print(ans2)


def ok(s, t, p, valid, nums):
    for a, b in zip("abcdefg", p):
        s = s.replace(a, b)
        t = t.replace(a, b)
    s = ' '.join([''.join(sorted(x)) for x in s.split()])
    t = ' '.join([''.join(sorted(x)) for x in t.split()])
    for n in s.split():
        if n not in valid:
            return -1
    sm = 0
    for n in t.split():
        if n not in valid:
            return -1
        sm *= 10
        sm += nums.index(n.lower())
    return sm


if __name__ == '__main__':
    main()
