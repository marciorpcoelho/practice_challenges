# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


def main():
    number = int(input('Please select a number (press Enter after the number): '))
    divisors = []

    for i in range(1, number + 1):
        if not number % i:
            divisors.append(i)
            # print()
    if len(divisors) == 2:
        print(str(number) + ' is a prime number, therefore its only divisors are ' + str(divisors))
    else:
        [print(str(x) + ' is a divisor of ' + str(number)) for x in divisors]


if __name__ == '__main__':
    main()
