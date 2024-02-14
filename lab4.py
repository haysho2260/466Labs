
def knn(x, k, points):
    dist = []
    if not (x >= 0 and x <= 4):
        raise ValueError("Input x must be in the range [0, 4]") 
    if not (k > 1 and k < 5):
        raise ValueError("Input x must be in the range (0,5)")
    for p in points:
        dist.append((abs(p[0] - x), p))
    sort_points =  sorted(dist, key=lambda pair: (pair[0], pair[1][0]))[:k]
    closest_ys = [pair[1][1] for pair in sort_points[:k]]
    return sum(closest_ys)/len(closest_ys)



if "__main__" == __name__:
    points = [(1,1), (2,2), (0,0), (4,4), (3,3)]
    x = 2
    k = 4
    print(knn(x, k, points))