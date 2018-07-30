# Challenge 02
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


def main():
    number = input('Please select a number (press Enter after number) ')

    # Check oddity
    if int(number) % 2:
        print('Chosen number is odd.')
    else:
        print('Chosen number is even.')
        if not int(number) % 4:
            print('Chosen number is also multiple of 4.')

    number_2 = input('Please select another number (press Enter after number) ')

    # Check multiplicity
    if int(number_2) > int(number):
        if int(number_2) % int(number):
            print('Number ' + number_2 + ' is not a multiple of ' + number + '.')
        else:
            print('Number ' + number_2 + ' is a multiple of ' + number + '.')
    elif int(number_2) < int(number):
        if int(number) % int(number_2):
            print('Number ' + number_2 + ' is not a divisor of ' + number + '.')
        else:
            print('Number ' + number_2 + ' is a divisor of ' + number + '.')
    elif int(number_2) == int(number):
        print('Both numbers are the same. They are simultaneously their own divisor and multiple.')


if __name__ == '__main__':
    main()