
def main():
    for _ in range(int(input())):
        n = int(input())
        inp = [int(i)-1 for i in input().split()]
        res = []
        for i in range(n):
            count = 1
            j = inp[i]
            while i != j:
                count += 1
                j = inp[j]
            res.append(count)
        print(str(res[0]), end = "")
        for i in res[1:]:
            print(" " + str(i), end = "")
        print()



if __name__ == "__main__":
    main()