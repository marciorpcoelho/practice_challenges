import time
import random
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.


def main():
    password_strength = input('Please choose the strength of the password (Weak/Medium/Strong): ')
    if password_strength == 'Weak':
        password_size = random.randint(4, 6)
    if password_strength == 'Medium':
        password_size = random.randint(7, 9)
    if password_strength == 'Strong':
        password_size = random.randint(10, 12)

    password = random_generator(password_size, password_strength)

    print(password_strength + ' password:', password)


def random_generator(password_size, strength):
    letter_password = []
    while len(letter_password) < password_size:
        if strength == 'Weak':
            letter_password.append(random.choice('abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ'))
        if strength == 'Medium':
            letter_password.append(random.choice('abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ0123456789'))
        if strength == 'Strong':
            letter_password.append(random.choice('abcdefghijklmnopqrstuvxywzABCDEFGHIJKLMNOPQRSTUVXYWZ0123456789!"#$%&/()=?@£{[]}+*'))
    return ''.join(letter_password)





if __name__ == '__main__':
    start = time.time()
    main()
    print('Running time is %.2f' % (time.time() - start))