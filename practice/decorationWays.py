from math import factorial
def rec(n, r, g, b):
    if r < 0 or g < 0 or b < 0:
        return 0
    if n == 1:
        return sum([1 if r else 0, 1 if g else 0, 1 if b else 0])
    d2, d3 = n // 2 if not n % 2 else 0, n // 3 if not n % 3 else 0
    ans = rec(n - 1, r - n, g, b) + rec(n - 1, r, g - n, b) + rec(n - 1, r, g, b - n)
    if d2:
        ans += (factorial(n) // (factorial(d2) * factorial(d2))) * (rec(n - 1, r - d2, g - d2, b) + rec(n - 1, r - d2, g, b - d2) + rec(n - 1, r, g - d2, b - d2))
    if d3:
        ans += (factorial(n) // (factorial(d3) * factorial(d3) * factorial(d3))) * rec(n - 1, r - d3, g - d3, b - d3)
    return ans


def main():
    print(rec(int(input()), int(input()), int(input()), int(input())))
    return


if __name__ == "__main__":
    main()
