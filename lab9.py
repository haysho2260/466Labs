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
                paths.append(((row[1], row[2], row[3]), float(row[0])))

    return gamma, reward, paths

def markov(gamma, reward, paths, prev):
    res = {}
    temp = {}
    idealAction ={}
    for key, v in reward.items():
        matching_values = [((pair[0][1], pair[0][2]), pair[1]) for pair in paths if pair[0][0] == key]
        pathPerAction = {}
        for item in matching_values:
            k = item[0][0]
            if k not in pathPerAction:
                pathPerAction[k] = {}
            pathPerAction[k][item[0][1]] = item[1]

        outputLists = [{k: value} for k, value in pathPerAction.items()]
        
        for outputList in outputLists:
            temp[key] = v
            for val_key, val_value in outputList.items():
                for action, discount in val_value.items():
                    temp[key] += (gamma * prev[action] * discount)
                    if key in res and res[key] < temp[key] or not key in res:
                        res[key] = round(temp[key], 2)
                        idealAction[key] = val_key       
    return res, idealAction

if __name__ == "__main__":
    gamma, reward, paths = read_csv('lab8data.csv')

    prev = reward
    temp, idealAction = markov(gamma, reward, paths, prev)
    while prev != temp:
        prev = temp
        temp, idealAction = markov(gamma, reward, paths, prev)
    
    # for key, value in temp.items():
    #     print(f"'{key}': {value}")
    
    print("Ideal Action:")
    for key, value in idealAction.items():
        print(f"'{key}': {value}")