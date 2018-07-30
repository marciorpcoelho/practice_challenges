import datetime
# Challenge 01

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)'


def main():
    name = input('What is your name? (press Enter after name) ')
    age = input('What is your age? (press Enter after age) ')
    birthday_check = input('Has your birthday passed yet? (Yes or No) ')
    number = input('Please choose a random number. (press Enter after number) ')

    birth_year = function_birth_year(age, birthday_check)
    # repeated_message(number)

    for i in range(int(number)):
        print('Your name is ' + name + ' and you were born in ' + str(birth_year) + ' and you will be 100 years old in the year ' + str(birth_year + 100) + '. ' + str(i+1) + '/' + number + '\n')


def function_birth_year(age, birthday_check):
    birth_year = datetime.datetime.now().year - int(age)

    if birthday_check == 'No':
        birth_year -= 1

    return birth_year


if __name__ == '__main__':
    main()