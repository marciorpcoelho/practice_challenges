import numpy as np
import numpy.random as nprnd
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.


def main():
    a = nprnd.randint(10, size=15)
    print('Original List ', a)
    remove_dups_method1(a)
    remove_dups_method2(a)
    remove_dups_method3(a)


def remove_dups_method1(a):
    print('Without duplicates Method 1:', np.unique(a))


def remove_dups_method2(a):
    new_list = []
    for value in a:
        if value not in new_list:
            new_list.append(value)
    print('Without duplicates Method 2:', new_list)


def remove_dups_method3(a):
    print('Without duplicates Method 3:', list(set(a)))


if __name__ == '__main__':
    main()
