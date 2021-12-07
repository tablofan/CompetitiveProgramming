def main():
    with open('input.txt', 'r') as file:
        lines = [int(i) for i in file.readlines()[0].split(",")]
    fuel = 10000000000000
    t = 0
    for i in range(200,2000):
        for j in lines:
            a = abs(j-i)
            t += (a*(a+1))/2
        if t<fuel:
            fuel = t
        t = 0
    print(fuel)


if __name__ == '__main__':
    main()
