import numpy.random as nprnd
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.


def main():
    a = nprnd.randint(100, size=15)
    print('Random List is ', a)
    new_list = first_and_last_value(a)
    print('The new list is ', new_list)


def first_and_last_value(a):
    return [a[0], a[-1]]


if __name__ == '__main__':
    main()
