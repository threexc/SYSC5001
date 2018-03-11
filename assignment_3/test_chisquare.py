#/usr/bin/python3

from scipy.stats import chisquare
from math import ceil


def test_chisquare(observed_data_filename):
    data_set = []
    counts = [0]*10
    with open(observed_data_filename) as f:
        for line in f:
            data_set.append(float(line.strip('\n').replace('"','')))
    f.close()
    #print(data_set)
    #print(chisquare(data_set))

    #print(len(counts))
    for number in data_set:
        if (number > 0) and (number <= 0.1):
            counts[0] = counts[0] + 1
        elif (number > 0.1) and (number <= 0.2):
            counts[1] = counts[1] + 1
        elif (number > 0.2) and (number <= 0.3):
            counts[2] = counts[2] + 1
        elif (number > 0.3) and (number <= 0.4):
            counts[3] = counts[3] + 1
        elif (number > 0.4) and (number <= 0.5):
            counts[4] = counts[4] + 1
        elif (number > 0.5) and (number <= 0.6):
            counts[5] = counts[5] + 1
        elif (number > 0.6) and (number <= 0.7):
            counts[6] = counts[6] + 1
        elif (number > 0.7) and (number <= 0.8):
            counts[7] = counts[7] + 1
        elif (number > 0.8) and (number <= 0.9):
            counts[8] = counts[8] + 1
        else:
            counts[9] = counts[9] + 1

    print("The observed frequencies in each interval of length 0.1: " + str(counts) + "\n")

    print(chisquare(counts, [10,10,10,10,10,10,10,10,10,10]))

"""
def evaluate_uniform_data_set(data_set, num_intervals):
    counts = [0]*num_intervals
    interval_length = ceil(max(data_set)) / num_intervals

    for number in data_set:
        if (number >= 0) and (number < interval_length):
            counts[0] = counts[0] + 1
        elif (number >= interval_length) and (number < 2*interval_):
            counts[1] = counts[1] + 1
        elif (number >= 0.2) and (number < 0.3):
            counts[2] = counts[2] + 1
        elif (number >= 0.3) and (number < 0.4):
            counts[3] = counts[3] + 1
        elif (number >= 0.4) and (number < 0.5):
            counts[4] = counts[4] + 1
        elif (number >= 0.5) and (number < 0.6):
            counts[5] = counts[5] + 1
        elif (number >= 0.6) and (number < 0.7):
            counts[6] = counts[6] + 1
        elif (number >= 0.7) and (number < 0.8):
            counts[7] = counts[7] + 1
        elif (number >= 0.8) and (number < 0.9):
            counts[8] = counts[8] + 1
        else:
            counts[9] = counts[9] + 1


"""
if __name__ == "__main__":
    # execute only if run as a script
    test_chisquare("swapped.txt")
    test_chisquare("7_8_data")
