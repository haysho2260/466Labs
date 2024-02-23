import csv
import math


def read_csv(csv_path):
    """ reads in csv with file data"""
    # Initialize empty lists for each column
    outlook = []
    temperature = []
    humidity = []
    wind = []
    play_tennis = []

    # Open the CSV file and read its contents
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        # Skip the header row
        next(csv_reader)
        # Iterate over each row in the CSV
        for row in csv_reader:
            # Append each element of the row to the corresponding column list
            outlook.append(row[0].lower())
            temperature.append(row[1].lower())
            humidity.append(row[2].lower())
            wind.append(row[3].lower())
            play_tennis.append(row[4].lower())

    return outlook, temperature, humidity, wind, play_tennis


def info_gain(children, parent):
    """
    Calculates the information gain of a given attribute 
    (parent), when used to split a dataset of children.
    """
    
    # find the entropy of the parent
    parent_entropy = find_entropy(parent)
    all_info_gain = []
    
    # calculate the info gain per child
    for key, lst in children.items():
        
        # initialize value starting off with parent entropy
        temp_value = parent_entropy
        
        # get list of choices
        choices = set(lst)
        total_len = len(parent)

        # calculat entropy for each option
        for choice in choices:
            choice_indices = [index for index, value in enumerate(lst) if value == choice]
            
            # make list from parent based on choice indices
            new_list = [parent[i] for i in choice_indices]

            # subtract fraction * entropy 
            temp_value -= (len(new_list)/total_len) * find_entropy(new_list)
        # append new info gain
        all_info_gain.append((key, round(temp_value, 3)))
    
    # return sorted list of best most to least info gain
    return sorted(all_info_gain, key=lambda x: x[1], reverse=True)


def find_entropy(features):
    """ Finds the entropy H(X) given a set"""
    choices = set(features)
    total_len = len(features)
    res = 0
    for choice in choices:
        choice_fraction = features.count(choice) / total_len
        if choice_fraction != 0:
            res -= (choice_fraction) * math.log2(choice_fraction)
    return res


if "__main__" == __name__:
    outlook, temperature, humidity, wind, play_tennis = read_csv(
        'lab5data.csv')
    children = {"outlook": outlook, "temperature": temperature,
                "humidity": humidity, "wind": wind}
    info_gain_list = info_gain(children, play_tennis)
    print("\n", info_gain_list)
    print(f"\nThe max info gain is {info_gain_list[0][0]} with value {info_gain_list[0][1]}.\n")
