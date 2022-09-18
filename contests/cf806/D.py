def solve():
    n = int(input())
    word_list = [""] * n
    for i in range(n):
        word_list[i] = input()
    word_set = set(word_list)
    res = ["0"] * n
    for j in range(n):
        word = word_list[j]
        for i in range(1, len(word)):
            left = word[:i]
            right = word[i:]
            if left in word_set and right in word_set:
                res[j] = "1"
    print("".join(res))
    return


def main():
    for _ in range(int(input())):
        solve()
    return


if __name__ == "__main__":
    main()
