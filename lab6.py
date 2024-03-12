import csv
import math


def read_csv(csv_path):
    """ reads in csv with file data"""
    # Initialize empty lists for each column
    points = []

    # Open the CSV file and read its contents
    with open(csv_path, 'r') as file:
        csv_reader = csv.reader(file)
        # Skip the header row
        next(csv_reader)
        # Iterate over each row in the CSV
        for row in csv_reader:
            # Append each element of the row to the corresponding column list
            points.append([int(row[0]), int(row[1])])


    return points


def custom_sorting_key(point, reference_point):
    # First, sort by distance from reference point
    dist = abs(point[0] - reference_point[0])
    return dist

def mse(points, n):
    """
    Calculates the mse of loocv.
    """

    mse = 0
    
    for point in points:
        sorted_points = sorted(points, key=lambda p: custom_sorting_key(p, point))
        # Calculate the sum of y-values
        sum_y = sum(p[1] for p in sorted_points[1:n+1])

        # Calculate the average y-value
        avg_y = (sum_y / n)

        mse +=  ((avg_y-point[1]) ** 2)
    
    return mse/len(points)




if "__main__" == __name__:
    points = read_csv('lab6data.csv')
    n = int(input("Please input the value of n: "))
    mse = mse(points, n)
    print("\n", mse)
    print(
        f"\nThe means square error is {mse}\n")
