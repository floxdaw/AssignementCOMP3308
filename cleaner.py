import string


def one_string(string_array):
    new_string = ''
    for line in string_array:
        new_string = new_string + line

    return new_string


def save_capital(string):
    positions = []
    string = list(string)
    for idx, letter in enumerate(string):
        if letter.isupper():
            positions.append(idx)
        string[idx] = string[idx].lower()

    string = ''.join(string)
    return positions, string


def give_me_clean_string(input_string):
    all_one_line = one_string(input_string)
    positions, all_one_lower_line = save_capital(all_one_line)

    return positions, all_one_lower_line


def recapitalise(positions, string_lower):
    string_lower = list(string_lower)
    for position in positions:
        string_lower[position] = string_lower[position].upper()
    string_lower = ''.join(string_lower)
    return string_lower


def remove_nl_from_strings(dictionary):
    for idx, word in enumerate(dictionary):
        dictionary[idx] = word.strip()

    return dictionary


def factorize_letters(letters_string):
    letters_string = ''.join(sorted(letters_string))
    array = list(letters_string)
    pairs_array = []
    count = 0
    for reference_letter in range(len(array)):
        for following_letter in range(reference_letter + 1, len(array)):
            pairs_array.append([array[reference_letter].lower(), array[following_letter].lower()])
            count = count + 1

    return pairs_array


def clean_pair(pair, string):
    if (pair[0] in string) or (pair[1] in string):
        return True
    return False


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


def apply_pairs(pairs_array, string):
    nodes = {}

    for pair in pairs_array:
        local_string = string
        if clean_pair(pair, local_string):
            local_string = list(local_string)
            for idx, letter in enumerate(local_string):
                if letter == pair[0]:
                    local_string[idx] = pair[1]
                elif letter == pair[1]:
                    local_string[idx] = pair[0]
            local_string = ''.join(local_string)
        # print(pair, local_string)
        if local_string != string:
            nodes[str(pair)] = local_string

    return nodes


def find_max_depth(graph):  # this can be optimized to be embedded in the bfs function so that each loop calculates
    # this on the current node.
    max_depth = 0
    for key in graph:
        if graph[key].path_cost > max_depth:
            max_depth = graph[key].path_cost
    return max_depth


def return_all_strings_together(final_graph, max_fringe, positions, debug):
    max_depth = find_max_depth(final_graph)


    num_nodes_string = "Num nodes expanded: {}".format(len(final_graph))
    max_fringe_string = 'Max fringe size: {}'.format(max_fringe)
    max_depth_string = 'Max depth: {}'.format(max_depth)

    solution = False
    for key in final_graph:
        if final_graph[key].goal:
            solution = True

    if solution:
        solution_string = 'Solution: {}'.format(recapitalise(positions, final_graph[len(final_graph)].parent))
        key_string = "Key: {}\n".format((final_graph[len(final_graph)].key.replace(' ', '')).upper())
        path_cost_string = "Path Cost: {}\n\n".format(final_graph[len(final_graph)].path_cost)
    else:
        solution_string = 'No solution found.'
        key_string = ''
        path_cost_string = ""

    final_string = solution_string + '\n\n' + key_string  + path_cost_string + num_nodes_string + '\n' + max_fringe_string + '\n' + max_depth_string + '\n'

    if debug == 'y':
        count = 1
        first_expanded_states_string = "First few expanded states:"
        for key in final_graph:

            first_expanded_states_string = first_expanded_states_string + '\n' + recapitalise(positions,
                                                                                              final_graph[
                                                                                                  key].parent) + '\n'

            if count >= 10:
                break
            count = count + 1
        final_string = final_string + '\n' + first_expanded_states_string

    return final_string
