import numpy as np
# Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


def main():
    sample_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print('Sample list is ', sample_list)

    print('1st method:')
    for value in sample_list:
        if value < 5:
            print(value)

    print('2nd method:')
    new_list = [value for value in sample_list if value < 5]
    print(new_list)

    number = int(input('Please choose a number between ' + str(np.min(sample_list)) + ' and ' + str(np.max(sample_list)) + ' (press Enter after number) '))
    user_list = [x for x in sample_list if x < number]
    if user_list:
        print('The numbers of ' + str(sample_list) + ' which are smaller than ' + str(number) + ' are:')
    elif not user_list:
        print('The selected number is smaller than the minimum value of the list.')


if __name__ == '__main__':
    main()
