def main():
    for _ in range(int(input())):
        n, s = int(input()), input()
        l, c = 0, 0
        while l + 1 < n:
            if s[l] == '(' or (s[l] == ')' and s[l+1] == ')'):
                l += 2
            else:
                r = l + 1
                while r < n and s[r] != ')':
                    r += 1
                if r == n:
                    break
                l = r + 1
            c += 1
        print(str(c)+" "+str(n-l))


if __name__ == "__main__":
    main()