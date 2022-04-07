def en_de_crypt(list_of_lines, key):
    for step in range(0, len(key) - 1, 2):
        swap_1 = key[step].lower()
        swap_2 = key[step + 1].lower()
        # print(swap_1, swap_2, list_of_lines)
        for line_num in range(0, len(list_of_lines)):
            string = list(list_of_lines[line_num])
            for i in range(len(string) - 1):
                if string[i] == swap_2:
                    string[i] = swap_1
                elif string[i] == swap_1:
                    string[i] = swap_2
                elif string[i].upper() == swap_1.upper():
                    string[i] = swap_2.upper()
                elif string[i].upper() == swap_2.upper():
                    string[i] = swap_1.upper()
            string_2 = ''.join(string)
            list_of_lines[line_num] = string_2

    output_string = ''.join(list_of_lines)
    return output_string


def task1(key, filename, indicator):
    usable_string = ''
    with open(filename) as f:
        usable_string = f.readlines()

    if indicator == 'd':
        key = key[::-1]
    elif indicator != 'e':
        return

    changed_string = en_de_crypt(usable_string, key)

    return changed_string


if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task1 function

    print(task1('VFSC', 'strange.txt', 'd'))
