# classification using 10-fold stratified cross-validation
from statistics import mean

import folds
import kNN
import NiaveBayes
import time


def predict_ai_avg(name, the_dict, k_flag):
    start = time.time()

    count = 1
    k = k_flag
    accuracy_array = []
    for z in range(len(the_dict)):
        test_set = []
        train_set = []
        saved_classes = []

        for key, item in the_dict.items():
            if key == count:
                for array in item:
                    test_set.append(array[:-1])
                    saved_classes.append(array[-1])

            else:
                for array in item:
                    train_set.append(array)
        if name == 'kNN':
            predict = kNN.classify_nn(train_set, test_set, k)
            count += 1
        elif name == 'Nbayes':
            predict = NiaveBayes.classify_nb(train_set, test_set)
            count += 1

        num_correct_predictions = 0
        if len(saved_classes) != len(predict):
            print("An error occurred wth the length")
        else:
            for idx, item in enumerate(saved_classes):
                if predict[idx] == item:
                    num_correct_predictions += 1

        print(str(num_correct_predictions) + '/' + str(len(saved_classes)) + ' --> ' + str(
            round(float(num_correct_predictions / len(saved_classes)) * 100, 2)))
        accuracy_array.append(float(num_correct_predictions / len(saved_classes)))
    end = time.time()
    total = end - start
    print('Time taken: ' + str(total))

    return mean(accuracy_array) * 100, total


fold_dict = folds.create_folded_data("pima.csv")

k_n = 5
avg_array = []
total_time = []
time_t_arr = []
for i in range(10):
    avg, time_t = predict_ai_avg('kNN', fold_dict, k_n)
    avg_array.append(avg)
    time_t_arr.append(time_t)
    print("Run {}".format(i+1))
total_avg = mean(avg_array)
print('Average over 10x 10 folds: ' + str(total_avg) + '\n' + str(sum(time_t_arr)))

avg_array = []
total_time = []
time_t_arr = []
for i in range(10):
    avg, time_t = predict_ai_avg('Nbayes', fold_dict, k_n)
    avg_array.append(avg)
    time_t_arr.append(time_t)
    print("Run {}".format(i + 1))
total_avg = mean(avg_array)
print('Average over 10x 10 folds: ' + str(total_avg) + '\n' + str(sum(time_t_arr)))
