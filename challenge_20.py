import numpy.random as nprnd
import numpy as np
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
#
# Extras:
# Use binary search.


def main():
    listing = np.sort(nprnd.randint(100, size=15))
    number = int(nprnd.randint(100, size=1))

    if easy_method(listing, number):
        print('Easy method: Number', number, 'is in the list ', listing)
    else:
        print('Easy method: Number', number, 'is not in the list ', listing)

    existence_check, iteration_count = binary_search(listing, number)
    if existence_check:
        print('Binary Search: Number', number, 'is in the list ', listing)
    else:
        print('Binary Search: Number', number, 'is not in the list ', listing)
    print('Number of Iterations:', iteration_count)


def easy_method(listing, number):
    if number in listing:
        return 1
    else:
        return 0


def binary_search(listing, number):
    iteration_count = 0
    while len(listing) != 1:
        position = round(len(listing) / 2)

        if number < listing[position]:
            iteration_count += 1
            listing = [listing[value] for value in range(position)]
        elif number > listing[position]:
            iteration_count += 1
            listing = [listing[value] for value in range(position, len(listing))]
        elif number == listing[position]:
            iteration_count += 1
            return 1, iteration_count

    return 0, iteration_count






if __name__ == '__main__':
    main()

