#works for both part 1 and part 2

def main():
    with open('input.txt', 'r') as file:
        lines = [int(i) for i in file.readlines()[0].split(",")]
    c = 0
    d = {i:lines.count(i) for i in range(9)} #dict with counts of starting numbers
    while c<256:
        temp = d[0]
        for i in range(1,9):
            d[i-1] = d[i]
        d[8] = temp
        d[6] += temp
        c+=1
    print(sum(d.values()))


if __name__ == '__main__':
    main()
