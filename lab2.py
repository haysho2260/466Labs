import math

'''
This function implements the basic execution of KMeans Clustering.
Given a list of points and a list of centroids, it gets a list of 
points that are closest to each centroid. It averages each list of 
points and returns that as the new centroid list. It continues to
loop through the K Means function until  there is no change in the 
centroids.
'''

def distance_formula(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def average_points(point_list):
    num_points = len(point_list)
    
    if num_points == 0:
        return None  # Handle the case when the list is empty
    
    sum_x = sum(point[0] for point in point_list)
    sum_y = sum(point[1] for point in point_list)
    
    avg_x = sum_x / num_points
    avg_y = sum_y / num_points
    
    return (avg_x, avg_y)

def kMeansClustering(points, centroids):
    points_closest = {}
    for point in points:
        # find the closest centroid per per point
        mn = centroids[0]
        mn_dist = None
        for centroid in centroids:
            temp_dist = distance_formula(point, centroid)
            if mn_dist is None or temp_dist < mn_dist:
                mn = centroid
                mn_dist = temp_dist
        if mn not in points_closest:
            points_closest[mn] = [point]
        else:
            points_closest[mn].append(point)
    res = []
    for list_points in points_closest.values():
        if list_points:
            res.append(average_points(list_points))
        
    return res
        
        

if __name__ == "__main__":
    points = [(1,1), (2,1), (0,1), (4,1), (4,2), (3,1)]
    centroids = [(1,5), (2,5)]
    newCentroids = kMeansClustering(points, centroids)
    
    while newCentroids != centroids:
        centroids, newCentroids = newCentroids, kMeansClustering(points, newCentroids)
    print(newCentroids)
    