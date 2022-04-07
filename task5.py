import cleaner as clnr
import math

def task5(message_filename, is_goal):


    with open(message_filename) as f:
        message = f.readlines()

    comparison_string = 'ETAONS'

    if is_goal:
        return 0
    else:

        letters_dict = {}

        positions, usable_string = clnr.give_me_clean_string(message)

        comparison_string = list(comparison_string.lower())
        for letter in comparison_string:
            letters_dict[letter] = 0
        usable_string = list(usable_string)

        for letter_letter in usable_string:
            if letter_letter in comparison_string:
                letters_dict[letter_letter] = letters_dict[letter_letter] + 1

        sorted_dict = dict(sorted(letters_dict.items(), key=lambda item: item[1]))





        unsorted_array =[]

        for k in sorted_dict.keys():
            unsorted_array.append([k, sorted_dict[k]])

        unsorted_array = unsorted_array[::-1]

        # TODO
        swap = True
        while swap:
            for i in range(len(unsorted_array)-1):
                swap = False
                if unsorted_array[i][1] == unsorted_array[i+1][1]:
                    if unsorted_array[i+1][0] < unsorted_array[i][0]:
                        tmp = unsorted_array[i+1][0]
                        unsorted_array[i+1][0] = unsorted_array[i][0]
                        unsorted_array[i][0] = tmp
                        swap = True


        sorted_arry = []
        for item in unsorted_array:
            sorted_arry.append(item[0])




        incorrect_pos = 0
        for idx, item in enumerate(sorted_arry):
            if item != comparison_string[idx]:
                incorrect_pos = incorrect_pos + 1

        incorrect_pos = math.ceil(incorrect_pos/2)
        return incorrect_pos



if __name__ == '__main__':
    # Example function calls below, you can add your own to test the task5 function
    #print(task5('freq_eg1.txt', False))
    #print(str(task5('freq_eg3.txt', False)) + ' my own')
    #print(task5('freq_eg1.txt', True))
    print(task5('freq_eg2.txt', False))
