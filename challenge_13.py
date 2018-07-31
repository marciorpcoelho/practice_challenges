# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


def main():
    sequence_limit = int(input('Please choose the size of the Fibonacci Sequence: '))

    fib_sequence = [1, 1]
    while len(fib_sequence) < sequence_limit:
        fib_sequence.append(fib_sequence[len(fib_sequence)-1] + fib_sequence[len(fib_sequence)-2])

    print(fib_sequence)


if __name__ == '__main__':
    main()
