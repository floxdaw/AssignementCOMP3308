import csv
import numpy as np
import statistics as stat
import math


def get_lovely_array(input_file):
    with open(input_file) as f:
        reader = csv.reader(f)
        data = list(reader)

    return data


###################### k-NN #############################

def yes_or_no(train_data, test_data, k):
    listy = create_distance_list(train_data, test_data)
    sorted_listy = sorted(listy, key=lambda x: x[0])

    num_yes = sum(x.count('yes') for x in sorted_listy[:k])
    num_no = sum(x.count('no') for x in sorted_listy[:k])

    if num_yes > num_no:
        return 'yes'
    elif num_yes < num_no:
        return 'no'
    else:
        return 'yes'


def create_distance_list(train_vector_list, test_vector):
    distance_list = []

    for current_vector in train_vector_list:
        distance, e_class = compute_distance(current_vector, test_vector)
        distance_list.append([distance, e_class])

    return distance_list


def compute_distance(vector_train, vector_test):
    e_class = vector_train[-1]

    a = np.asarray(vector_train[:-1])
    a = a.astype(float)
    b = np.asarray(vector_test)
    b = b.astype(float)
    distance = np.linalg.norm(a - b)

    return distance, e_class


########## Niave Bayes #################

def make_them_numbers(tran_data):
    number_array = []

    for row in tran_data:
        a = np.asarray(row)
        a = a.astype(float)
        number_array.append(list(a))

    return number_array


def separate_by_class(train_data):
    yes_no = {}
    for row in train_data:
        class_value = row[-1]
        if class_value not in yes_no:
            yes_no[class_value] = list()
        a = np.asarray(row[:-1])
        a = a.astype(float)
        yes_no[class_value].append(list(a))

    return yes_no


def summarize(train_data):
    mean_stdev_count = [(stat.mean(column), stat.stdev(column), len(column)) for column in zip(*train_data)]
    return mean_stdev_count


def summarize_by_class(train_data):
    summaries = {}
    for yes_no, rows in train_data.items():
        summaries[yes_no] = summarize(rows)
    return summaries


def gausian_prob(mean, stdev, x):
    exponent = math.exp(-0.5 * ((x - mean) / stdev) ** 2)
    f_x = (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

    return f_x


def class_probabilities(summaries, row):
    total_rows = sum([summaries[e_class][0][2] for e_class in summaries])
    probabilities = {}
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = summaries[class_value][0][2] / float(total_rows)
        for idx, value in enumerate(class_summaries):
            mean, stdev, count = value
            probabilities[class_value] *= gausian_prob(mean, stdev, row[idx])
    return probabilities


####### Writing file in correct format - Note the last 2 '\n' lines of the file need to be manually deleted
def write_folds(fold_dict):
    f = open("prima-folds.csv", "w")
    for key, item in fold_dict.items():
        f.write('fold' + str(key) + '\n')
        for array in item:
            for idx, value in enumerate(array):
                if idx < len(array) - 1:
                    f.write(str(value) + ',')
                else:
                    f.write(str(value))
            f.write('\n')
        f.write('\n')
    f.close()
