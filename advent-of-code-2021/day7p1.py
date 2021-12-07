def main():
    with open('input.txt', 'r') as file:
        lines = [int(i) for i in file.readlines()[0].split(",")]
    fuel = 1000000000
    t = 0
    for i in range(1000):
        for j in lines:
            t += abs(j-i)
        if t<fuel:
            fuel = t
        t = 0
    print(fuel)


if __name__ == '__main__':
    main()
