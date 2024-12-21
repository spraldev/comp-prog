from itertools import permutations

names = ["Beatrice", "Belinda", "Bella", "Betsy", "Blue", "Buttercup", "Sue", "Bessie"]
cow_pairs = []

result = []


with open("lineup.in", "r") as f:
    n = int(f.readline().strip())
    for i in range(n):
        line = f.readline().strip().split()
        cow_pairs.append((line[0], line[5]))

print()

def check(perm):
    passed = True

    for i in range(len(cow_pairs)):
        if abs(perm.index(cow_pairs[i][0]) - perm.index(cow_pairs[i][1])) != 1:
            passed = False
            break

        
    return passed

valid_permutations = []

for perm in permutations(names):
    if check(perm):
        valid_permutations.append(perm)


result = min(valid_permutations)

    

with open("lineup.out", "w") as f:
    for cow in result:
        f.write(cow + "\n")

    
