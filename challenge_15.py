# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.


def main():
    sentence = input('Please write a sentence with any number of words: ')

    # Approach 1
    sentence_list = remove_spaces(sentence)
    new_sentence_list = switch_order_method2(sentence_list)
    new_sentence = join_sentence(new_sentence_list)
    print('A1: The reversed sentence is:', new_sentence)

    # Approach 2
    print('A2: The reversed sentence is:', ' '.join(sentence.split()[::-1]))


def remove_spaces(sentence):
    return sentence.split()


def switch_order_method1(sentence_list):
    return list(reversed(sentence_list))


def switch_order_method2(sentence_list):
    new_list = []
    for i in range(len(sentence_list)):
        new_list.append(sentence_list[-i - 1])
    return new_list


def join_sentence(new_sentence_list):
    return ' '.join(new_sentence_list)


if __name__ == '__main__':
    main()
