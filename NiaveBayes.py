import routines as rt
import numpy as np


def classify_nb(training_filename, testing_filename):

    if isinstance(testing_filename, str):
        train_data = rt.get_lovely_array(training_filename)
        test_data = rt.get_lovely_array(testing_filename)
    elif isinstance(testing_filename, list):
        train_data = training_filename
        test_data = testing_filename


    two_classes = rt.separate_by_class(train_data)

    overall_summary_by_class = rt.summarize_by_class(two_classes)

    numerized_test_data = rt.make_them_numbers(test_data)

    class_array = []

    for row in numerized_test_data:
        probabilities = rt.class_probabilities(overall_summary_by_class, row)
        if probabilities['yes'] > probabilities['no']:
            class_array.append('yes')
        elif probabilities['yes'] < probabilities['no']:
            class_array.append('no')
        else:
            class_array.append('yes')

    return class_array


#print(classify_nb("prima_train.csv", "prima_test.csv"))
