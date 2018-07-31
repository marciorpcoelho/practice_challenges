# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.


def main():

    again = 'Yes'
    while again == 'Yes':
        user_input_int = user_input()
        divisors_list = divisors(user_input_int)
        if prime_check(divisors_list):
            print('Chosen value ' + str(user_input_int) + ' is prime.')
        else:
            print('Chosen value ' + str(user_input_int) + ' is not prime.')

        again = input('Play Again? (Yes/No) ')

    print('Thanks for playing!')


def user_input():
    user_input_int = int(input('Please choose a random number: '))
    return user_input_int


def divisors(value):
    divisors_list = [number for number in range(1, value + 1) if not value % number]
    return divisors_list


def prime_check(divisors_list):
    if len(divisors_list) == 2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    main()
