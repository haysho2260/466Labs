import csv

def read_csv(csv_path):
    """Reads in CSV with file data"""
    # Initialize empty lists for each column
    gamma = 0
    reward = {}
    paths = []
    temp = []
    # Open the CSV file and read its contents
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        # Skip the header row
        temp = []
        paths = []
        for i, row in enumerate(csv_reader):
            if i == 0:
                for j in row:
                    temp.append(j)
            elif i == 1:
                gamma = float(row[0])
                reward = {temp[j]: float(value) for j, value in enumerate(row[1:], start=1)}
            else:
                paths.append(((row[1], row[2]), float(row[0])))

    return gamma, reward, paths

def markov(gamma, reward, paths, prev):
    res = {}
    for key, v in reward.items():
        matching_values = {pair[0][1]: pair[1] for pair in paths if pair[0][0] == key}
        print(matching_values)
        res[key] = v
        for val_key, val_value in matching_values.items():
            res[key] += (gamma * prev[val_key] * float(val_value))
            print(gamma, prev[key], val_value)
        res[key] = round(res[key], 2)
    print(res)
    return res

if __name__ == "__main__":
    gamma, reward, paths = read_csv('lab7data.csv')
    print(gamma)
    print(reward)
    print(paths)
    prev = reward
    temp = markov(gamma, reward, paths, prev)
    while prev != temp:
        prev = temp
        temp = markov(gamma, reward, paths, prev)
    
    for key, value in temp.items():
        print(f"'{key}': {value}")
