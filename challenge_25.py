import numpy.random as nprnd
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any.
# A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
# Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.


def main():

    play_matrix = []
    for i in range(3):
        a = nprnd.randint(3, size=3)
        play_matrix.append(a)

    print(play_matrix)
    result = victory_conditions(play_matrix)
    if result:
        print('Player', result, 'won, congratulations!')


def victory_conditions(matrix):

    # horizontals:
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col]:
            return matrix[0][col]

    # verticals
    for row in range(3):
        if matrix[row][0] == matrix[row][1] == matrix[row][2]:
            return matrix[row][1]

    # diagonals
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        return matrix[0][0]
    if matrix[0][2] == matrix[1][1] == matrix[2][0]:
        return matrix[0][2]

    print('No one won, try again.')



if __name__ == '__main__':
    main()
