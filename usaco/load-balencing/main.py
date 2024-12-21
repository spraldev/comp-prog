points = []
n = 0
b = 0

with open("balancing.in", "r") as f:
    n, b = map(int, f.readline().strip().split())
    for _ in range(n):
        x, y = map(int, f.readline().split())
        points.append((x, y))




min_y = n
for i in range(n):
    
    #calculate the number of cows in each side
    x = points[i][0]
    y = points[i][1]
    cows = [0, 0, 0, 0]
    for j in range(n):
        if points[j][0] < x and points[j][1] < y:
            cows[0] += 1
        elif points[j][0] > x and points[j][1] < y:
            cows[1] += 1
        elif points[j][0] < x and points[j][1] > y:
            cows[2] += 1
        else:
            cows[3] += 1

    #calculate the maximum number of cows in one side

    max_cows = max(cows)

    #update the minimum number of cows
    min_y = min(min_y, max_cows)

print(min_y)