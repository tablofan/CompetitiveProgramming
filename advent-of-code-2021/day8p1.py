#you only need to count how many strings of lengths 2, 3, 4, or 7 in the part of the input after "|"
def main():
    with open('input.txt', 'r') as file:
        lines = [i.split("|")[1].rstrip("\n").lstrip().split() for i in file.readlines()]
    sum = 0
    for i in lines:
        for j in i:
            if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) == 7:
                sum += 1
    print(sum)



if __name__ == '__main__':
    main()
