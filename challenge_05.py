import numpy as np
import numpy.random as nprnd

# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


def main():

    # Pre-set lists:
    print('Pre-Set Lists:')
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print('List A:', a)
    print('List B:', b)

    for value_a in np.unique(a):
        if value_a in b:
            print(value_a, ' is present in both lists')

    # Random Lists:
    print('Random Lists:')
    a = nprnd.randint(10, size=10)
    b = nprnd.randint(10, size=15)
    print('a =', a, '\n', 'b =', b)

    common_values = [value for value in np.unique(a) if value in b]
    if common_values:
        print('Common Values:' + str(common_values))
    elif not common_values:
        print('No common values.')


if __name__ == '__main__':
    main()