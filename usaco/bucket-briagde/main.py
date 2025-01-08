barn = (0,0)
lake = (0,0)
rock = (0,0)

with open("buckets.in", "r") as f:
    for i in range(10):
        line = f.readline().strip()
        for j in range(10):
            if line[j] == "B":
                barn = (i+1, j+1)
            elif line[j] == "L":
                lake = (i+1, j+1)
            elif line[j] == "R":
                rock = (i+1, j+1)


path1 = abs(barn[0] - lake[0]) + abs(barn[1] - lake[1])


if barn[0] == rock[0] == lake[0] and (
	lake[1] < rock[1] < barn[1] or barn[1] < rock[1] < lake[1]
):
	path1 += 2

elif barn[1] == rock[1] == lake[1] and (
	lake[0] < rock[0] < barn[0] or barn[0] < rock[0] < lake[0]
):
	path1 += 2
     

with open("buckets.out", "w") as f:
    f.write(str(path1-1) + "\n")