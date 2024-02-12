import numpy as np

def hierarchicalCluster(a, lw_index, pts, points):
    if len(points) < 2:
        return
    b = np.ones((len(a) - 1, len(a) - 1))*999
    mn = 9999
    mn_index = ()
    new_pts = ()
    points.remove(pts[0])
    points.remove(pts[1])
    points.insert(0, pts)
    
    c, d = lw_index
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            index_i = i
            index_j = j
            if i >= j:
                continue
            elif i == 0:
                if j not in lw_index:
                    if j < c and j < d:
                        index_j += 1
                    elif j > c and j > d:
                        index_j -= 1
                    b[index_j][index_i] = min(a[c][j], a[j][c], a[d][j], a[j][d])
                    if b[index_j][index_i] < mn:
                        mn = b[index_j][index_i]
                        mn_index = (index_j, index_i)
                        new_pts = (points[index_j], points[index_i])
            elif i in lw_index or j in lw_index:
                continue
            else:                
                if i < c and i < d:
                    index_i += 1
                elif i > c and i > d:
                    index_i -= 1
                if j < c and j < d:
                    index_j += 1
                elif j > c and j > d:
                    index_j -= 1
                b[index_j][index_i] = min(a[j][i], a[i][j])
                print(index_j)
                if b[index_j][index_i] < mn:
                    mn = b[index_j][index_i]
                    mn_index = (index_j, index_i)
                    new_pts = (points[index_j], points[index_i])
                    
    displayNice(points, b)
    hierarchicalCluster(b, mn_index, new_pts, points)
            
def dist(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def displayNice(points, a):
    pt_str = []
    mx = 0
    for p in points:
        s = tuple_to_string(p)
        pt_str.append(s)
        mx = max(len(s), mx)
    
    print(" "*mx, spaced_tuple_to_string(pt_str, mx))
    for i in range(len(points)):
        print("{:{}s}".format(tuple_to_string(points[i]), mx), spaced_tuple_to_string(a[i], mx))
    print("\n")

def tuple_to_string(t):
    return "(" + ", ".join(str(0) if x == 9999 else str(x) for x in t) + ")"

def spaced_tuple_to_string(t, n):
    return " ".join("{:>{}}".format(0 if x == 999.0 else x, n) for x in t)

if __name__ == "__main__":
    points = [(1,1), (2,1), (0,1), (4,1), (4,2), (3,1)]
    # points = [(1,1), (2,1), (0, 1)]
    matrix_size = len(points)
    a = np.ones((matrix_size, matrix_size))*999
    mn = 9999
    lw_index = ()
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            a[j][i] = round(dist(points[i], points[j]), 3)
            if  a[j][i] < mn:
                mn = a[j][i]
                lw_index = (j, i)
                pts = (points[j], points[i])
    displayNice(points, a)
    hierarchicalCluster(a, lw_index, pts, points)