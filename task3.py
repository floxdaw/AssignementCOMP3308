import cleaner as cleaner
import string


def checker(message, dictionary):
    words_array = message.split()
    length_of_string = len(words_array)

    for idx, word in enumerate(words_array):
        words_array[idx] = word.translate(str.maketrans('', '', string.punctuation))

    correct_count = 0
    for words in words_array:
        for item in dictionary:
            if words == item:
                correct_count = correct_count + 1
    ratio = round((correct_count / length_of_string) * 100, 2)
    return ratio


def task3(message_filename, dictionary_filename, threshold):
    with open(message_filename) as f:
        message = f.readlines()

    with open(dictionary_filename) as p:
        dictionary = p.readlines()

    positions, message = cleaner.give_me_clean_string(message)
    dictionary = cleaner.remove_nl_from_strings(dictionary)
    ratio = checker(message, dictionary)

    if ratio >= threshold:
        return (str('True\n{:.2f}'.format(ratio)))
    else:
        return (str('False\n{:.2f}'.format(ratio)))


if __name__ == '__main__':
    # print(task3('jingle_bells.txt', 'dict_xmas.txt', 90))
    print(task3('fruit_ode.txt', 'dict_fruit.txt', 80))
    # print(task3('amazing_poetry.txt', 'common_words.txt', 95))
