import numpy.random as nprnd
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)


def main():
    a = int(nprnd.randint(9, size=1))
    guess = int(input('I\'ve chosen a random number between 1 and 9. Care to guess it? '))
    guess_count = 1

    while guess != a:
        if guess == a:
            break

        if guess > a:
            print('Too high!')
        elif guess < a:
            print('Too low!')

        guess = int(input('New guess? '))
        guess_count += 1

    print('After ' + str(guess_count) + ' tries, that\'s right, Congratulations!')


if __name__ == '__main__':
    main()
