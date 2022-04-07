import cleaner as clnr
import searches as s


def task4(algorithm, message_filename, dictionary_filename, threshold, letters, debug):
    with open(message_filename) as f:
        message = f.readlines()

    with open(dictionary_filename) as p:
        dictionary = p.readlines()

    pairs_arr = clnr.factorize_letters(letters)

    positions, message = clnr.give_me_clean_string(message)
    dictionary = clnr.remove_nl_from_strings(dictionary)

    if algorithm == 'b':
        final_graph, max_fringe = s.BFS(message, dictionary, pairs_arr, threshold)

        final_string = clnr.return_all_strings_together(final_graph, max_fringe, positions, debug)


    elif algorithm == 'd':
        final_graph, max_fringe = s.DFS(message, dictionary, pairs_arr, threshold)
        max_depth = clnr.find_max_depth(final_graph)
        final_string = clnr.return_all_strings_together(final_graph, max_fringe, positions, debug)


    elif algorithm == 'i':
        s.IDS()


    elif algorithm == 'u':
        s.UCS()

    return final_string.strip()


if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task4 function
     #print(task4('d', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
    # print(task4('b', 'ai.txt', 'common_words.txt', 100, 'VFSC', 'y'))

    #print(task4('d', 'cabs.txt', 'common_words.txt', 100, 'ABC', 'y'))
     print(task4('b', 'spain.txt', 'common_words.txt', 80, 'ADE', 'y'))
