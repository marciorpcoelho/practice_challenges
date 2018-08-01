# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.
#
# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
#
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
#
# Remember that in Python 3, printing to the screen is accomplished by
#
#   print("Thing to show on screen")
# Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere on the Internet, like this TutorialsPoint link.


def main():
    size = int(input('What is the size of the board to print? '))

    # Method 1
    # method_1(size)
    method_2(size)


def method_1(size):
    for j in range(size):
        horizontals, verticals = str(), str()
        for i in range(size):
            horizontals += str(' ---')
            verticals += str('|   ')
        verticals += str('|')
        print(horizontals)
        print(verticals)
    print(horizontals)


def method_2(size):
    horizontals = str(' ---' * size)
    verticals = str('|   ' * (size + 1))

    for i in range(size):
        print(horizontals)
        print(verticals)
    print(horizontals)




if __name__ == '__main__':
    main()
