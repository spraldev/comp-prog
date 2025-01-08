a, b, x, y = 0, 0, 0, 0

with open("teleport.in", "r") as file:
    a, b, x, y = map(int, file.readline().split())


min_distance = abs(a - b)

dist1 = abs(x - a) + abs(y - b)
dist2 = abs(x - b) + abs(y - a)


with open("teleport.out", "w") as file:
    file.write(str(min(min_distance, dist1, dist2)))

