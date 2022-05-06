import routines as rt
import random


def create_folded_data(filename):
    data = rt.get_lovely_array(filename)

    random.shuffle(data)

    sorted_data = sorted(data, key=lambda x: x[-1])

    fold_dict = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: []

    }

    counter = 0
    while len(sorted_data) > 0:

        fold_dict[10 - counter].append(sorted_data.pop())
        counter += 1

        if counter > 9:
            counter = 0

    rt.write_folds(fold_dict)

    return fold_dict


