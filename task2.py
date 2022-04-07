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


def save_capital(string_array):
    positions = []
    for idx, row in enumerate(string_array):
        for idx_2, letter in enumerate(row):
            if letter.isupper():
                positions.append([idx, idx_2])
        string_array[idx] = string_array[idx].lower()
    return positions, string_array


def recapitalise(positions, string_array):
    for position in positions:
        string = list(string_array[position[0]])
        string[position[1]] = string[position[1]].upper()
        string = ''.join(string)
        string_array[position[0]] = string

    return string_array


def clean_pair(pair, string_array):
    for string in string_array:
        if (pair[0] in string) or (pair[1] in string):
            return True
    return False


def apply_pairs(pairs_array, string_array):
    nodes = {}


    for pair in pairs_array:
        local_string_array = string_array.copy()
        if clean_pair(pair, local_string_array):
            for line_idx, line in enumerate(local_string_array):
                string = list(line)
                for idx, letter in enumerate(string):
                    if letter == pair[0]:
                        string[idx] = pair[1]
                    elif letter == pair[1]:
                        string[idx] = pair[0]
                local_string_array[line_idx] = ''.join(string)
        #print(pair, local_string_array)
        if local_string_array != string_array:
            nodes[str(pair)] = local_string_array.copy()

    return nodes

def build_string_from_dict(dict):
    string = []
    string.append(str(len(dict)))
    string.append('\n')
    for key in dict:
        string.append(''.join(dict[key]))
        string.append("\n\n")

    string = ''.join(string)
    return string

def task2(filename, letters):
    with open(filename) as f:
        usable_string = f.readlines()

    possible_pairs = factorize_letters(letters)
    positions, lower_strings = save_capital(usable_string)


    dict = apply_pairs(possible_pairs, lower_strings)

    for key in dict:
        dict[key] = recapitalise(positions, dict[key])

    final_string = build_string_from_dict(dict)

    return final_string


if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task2 function
    print(task2('spain.txt', 'ABE'))
    #print(task2('ai.txt', 'XZ'))
    #print(task2('cabs_plain.txt', 'ABZD'))

#current issues - it tacks the original string on the end if there are no swaps made because the letters arent in the string
