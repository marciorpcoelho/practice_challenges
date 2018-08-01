# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
#
# (If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
# The explanation is easier with an example, which I will describe below.)


def main():

    primes = file_reading_to_list('primenumbers')
    happy = file_reading_to_list('happynumbers')

    overlap = [value for value in primes if value in happy]
    print(overlap)


def file_reading_to_list(file_name):
    lista = []
    with open(file_name + '.txt', 'r') as open_file:
        line = open_file.readline().strip()
        while line:
            lista.append(int(line))
            line = open_file.readline().strip()

    return lista


if __name__ == '__main__':
    main()
