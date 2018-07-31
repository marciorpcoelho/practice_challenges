import math
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)


def main():
    string = input('Please write any word/string (press Enter after): ')
    different_check = 0

    for i in range(math.floor(len(string) / 2)):
        if string[i] != string[-i-1]:
            different_check = 1
            print('The selected string is not palindrome.')
            break

    if not different_check:
        print('The select string is palindrome.')


if __name__ == '__main__':
    main()
