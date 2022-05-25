def rotate90(sol):
    res = ["" for _ in range(8)]
    for i,v in enumerate(sol):
        res[7 - col.index(v)] = col[i]
    return "".join(res)


def main():
    fundamentals = ["faebhcgd", "afhcgdbe", "aehfcgbd", "begachfd", "begdahfc", "bfagdhce", "bfhcadge", "bgcfhead",
                    "bgehadfc", "cehdagbf", "cfbehagd", "cebhagdf"]
    s = set(fundamentals)
    for i in fundamentals:
        s.add(rotate90(i))
        s.add(rotate90(rotate90(i)))
        s.add(rotate90(rotate90(rotate90(i))))
        s.add(i[::-1])
        s.add(rotate90(i)[::-1])
        s.add(rotate90(rotate90(i))[::-1])
        s.add(rotate90(rotate90(rotate90(i)))[::-1])
    s = [set(str(v) + str(i+1) for i,v in enumerate(j)) for j in s]
    inp = [input() for _ in range(8)]
    reserved = []
    for i in range(8):
        for j in range(8):
            if inp[i][j] == '*':
                reserved.append(col[j]+row[i])
    res = 92
    for j in s:
        for i in reserved:
            if i in j:
                res -= 1
                break
    print(res)
    return


if __name__ == "__main__":
    col = "abcdefgh"
    row = "12345678"

    main()