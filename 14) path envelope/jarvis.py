from math import sqrt
def jarvis_algoritm(points):
    x_list = []
    y_list = []
    list_result = []
    for point in points:
        x_list.append(point[0])
        y_list.append(point[1])
    for i in range(len(points)):
        if x_list[i] == min(x_list) and y_list[i] == min(y_list):
            p = points[i]
    list_result.append(p)
    index = points.index(p)
    x = index
    while True:
        q = (x+1)% len(points)

        for r in range(len(points)):
            if r == x:
                continue
            sigma = direction(points[x],points[q],points[r])
            if sigma  > 0:
                q = r
        list_result.append(points[q])
        x = q
        if x == index:
            break
        

    return list_result

def jarvis_2(points):
    x_list = []
    y_list = []
    list_result = []
    for point in points:
        x_list.append(point[0])
        y_list.append(point[1])
    for i in range(len(points)):
        if x_list[i] == min(x_list) and y_list[i] == min(y_list):
            p = points[i]
    list_result.append(p)
    index = points.index(p)
    x = index
    while True:
        q = (x+1)% len(points)
        for r in range(len(points)):
            if r == x:
                continue
            sigma = direction(points[x],points[q],points[r])
            if sigma  > 0 or (sigma == 0 and distance(points[r],points[x]) > distance(points[q],points[x])):
                q = r
        list_result.append(points[q])
        x = q
        if x == index:
            break
        
    return list_result

def direction(p1,p2,p3):
    sigma = (p2[1]-p1[1]) * (p3[0]-p2[0]) - (p3[1]-p2[1]) * (p2[0]-p1[0])
    return sigma

def distance(p1,p2):
    d = sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
    return d
    

def main():
    points_1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    points_2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    points_3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    print(jarvis_algoritm(points_1))
    print(jarvis_algoritm(points_2))
    print("Jarvis version 1")
    print(jarvis_algoritm(points_3))
    print("Jarvis version 2")
    print(jarvis_2(points_3))
if __name__ == "__main__":
    main()
