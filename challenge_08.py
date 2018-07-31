# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)


def main():

    win_condition = False
    print('Plays are: Rock, Paper, Scissor')
    while not win_condition:
        input_1 = input('Player 1 - Please choose your play: ')
        input_2 = input('Player 2 - Please choose your play: ')

        if input_1 == input_2:
            print('That is a draw.')

        if input_1 == 'Rock' and input_2 == 'Scissor':
            print('Player 1 Won, Congratulations!')
        elif input_2 == 'Rock' and input_1 == 'Scissor':
            print('Player 2 Won, Congratulations!')

        if input_1 == 'Scissor' and input_2 == 'Paper':
            print('Player 1 Won, Congratulations!')
        elif input_2 == 'Scissor' and input_1 == 'Paper':
            print('Player 2 Won, Congratulations!')

        if input_1 == 'Paper' and input_2 == 'Rock':
            print('Player 1 Won, Congratulations!')
        elif input_1 == 'Rock' and input_2 == 'Paper':
            print('Player 2 Won, Congratulations!')

        if play_again_check():
            print('Thanks for playing!')
            break


def play_again_check():
    input_3 = input('Want to play again? (Yes/No) ')
    if input_3 == 'No':
        return 1


if __name__ == '__main__':
    main()
