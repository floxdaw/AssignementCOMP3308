import routines as rt


def classify_nn(training_filename, testing_filename, k):

    if isinstance(testing_filename, str):
        train_data = rt.get_lovely_array(training_filename)
        test_data = rt.get_lovely_array(testing_filename)
    elif isinstance(testing_filename, list):
        train_data = training_filename
        test_data = testing_filename

    class_array = []
    for array in test_data:
        class_array.append(rt.yes_or_no(train_data, array, k))



    return class_array


#print(classify_nn("prima_train.csv", "prima_test.csv", 3))