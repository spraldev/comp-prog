points = []
N = 0


with open('balancing.in', 'r') as f:
    N = int(f.readline().strip())
    for _ in range(N):
        x, y = map(int, f.readline().strip().split())
        points.append((x, y))

def count_points(x, y):
   q1, q2, q3, q4 = 0, 0, 0, 0
   for point in points:
       if point[0] > x and point[1] > y:
           q1 += 1
       elif point[0] < x and point[1] > y:
           q2 += 1
       elif point[0] < x and point[1] < y:
           q3 += 1
       else:
           q4 += 1
   return max(q1, q2, q3, q4)

def count_points_y(y):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for point in points:
        if point[1] > y:
            q1 += 1
        else:
            q3 += 1
    return abs(q1 - q3)


def count_points_x(x):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for point in points:
        if point[0] > x:
            q1 += 1
        else:
            q2 += 1
    return abs(q1 - q2)





x_values = sorted([point[0] for point in points])
#x_values = [x_values[i] for i in range(len(x_values)) if i == 0 or x_values[i] != x_values[i - 1] and x_values[i] - x_values[i - 1] > 2]
y_values = sorted([point[1] for point in points])
#y_values = [y_values[i] for i in range(len(y_values)) if i == 0 or y_values[i] != y_values[i - 1] and y_values[i] - y_values[i - 1] > 2]

print(x_values)
print(y_values)


x_res = {}

for i in range(1, len(x_values)):
    x = (x_values[i] - x_values[i - 1]) / 2 + x_values[i - 1]
    x_res[i] = count_points_x(x)

y_res = {}

for i in range(1, len(y_values)):

    y = (y_values[i] - y_values[i - 1]) / 2 + y_values[i - 1]
    y_res[i] = count_points_y(y)



# x_values and y_values should equal the least 100 x and y values based on the x_res and y_res dictionaries

x_values = sorted([x_values[i] for i in sorted(x_res, key=x_res.get)[:150]])
y_values = sorted([y_values[i] for i in sorted(y_res, key=y_res.get)[:150]])

print(x_values)
print(y_values)






result = float('inf')

for i in range(1, len(x_values)):
    x = (x_values[i] - x_values[i - 1]) / 2 + x_values[i - 1]

    for j in range(1, len(y_values)):
        y = (y_values[j] - y_values[j - 1]) / 2 + y_values[j - 1]

        result = min(result, count_points(x, y))


with open('balancing.out', 'w') as f:
    f.write(str(result) + '\n')