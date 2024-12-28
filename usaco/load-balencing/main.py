points = []
N = 0
B = 0

with open('balancing.in', 'r') as f:
    N, B = map(int, f.readline().split())
    for _ in range(N):
        x, y = map(int, f.readline().split())
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


x_values = sorted([point[0] for point in points])
y_values = sorted([point[1] for point in points])

result = float('inf')

for i in range(N):
    if i == 0:
        continue;

    x = (x_values[i] - x_values[i - 1]) / 2 + x_values[i - 1]

    for j in range(N):
        if j == 0:
            continue;

        y = (y_values[j] - y_values[j - 1]) / 2 + y_values[j - 1]

        result = min(result, count_points(x, y))


with open('balancing.out', 'w') as f:
    f.write(str(result) + '\n')