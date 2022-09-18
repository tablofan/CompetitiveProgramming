def main():
    a = set(list("1234567890"))
    b = set(list("abcdefghijklmnopqrstuvwxyz"))
    c = set(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    d = set(list("#@*&"))
    for n in range(int(input())):
        input()
        num = False
        lower = False
        special = False
        upper = False

        s = list(input())
        for i in s:
            if i in a:
                num = True
            elif i in b:
                lower = True
            elif i in c:
                upper = True
            else:
                special = True
        if not num:
            s += "1"
        if not lower:
            s += "a"
        if not upper:
            s += "A"
        if not special:
            s += "#"
        while len(s) < 7:
            s += "a"
        s = "".join(s)
        print(f'Case #{n+1}: {s}')


if __name__ == "__main__":
    main()