from itertools import accumulate
def main():
    n, q = map(int, input().split())
    price = [int(i) for i in input().split()]
    price.sort(reverse=True)
    pref = [0] + list(accumulate(price))
    # print(pref)
    for _ in range(q):
        x, y = map(int, input().split())

        # print(f'{price[x-y:x] = }')
        print(pref[x] - pref[x-y])

    return


if __name__ == "__main__":
    main()
