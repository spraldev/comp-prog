N = 0
animals = {}

with open("guess.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        line = f.readline().strip().split()
        animal = line[0]
        features = line[2:]
        animals[animal] = features

print(animals)

common_count = {}

for animal in animals:
    common_count[animal] = 0
    common_arr = []

    for animal2 in animals:
        if animal == animal2:
            continue
        common_elems = [x for x in animals[animal] if x in animals[animal2]]

        if len(common_elems) > len(common_arr):
            common_arr = common_elems
    
    
    common_count[animal] = len(common_arr)





max_common = 0
max_common_animal = ""
for animal in common_count:
    if common_count[animal] > max_common:
        max_common = common_count[animal]
        max_common_animal = animal



with open("guess.out", "w") as f:
    f.write(str(max_common + 1) + "\n")