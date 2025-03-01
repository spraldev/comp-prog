
from math import ceil
n = 0

cities = []
states = []

pairs = {}

count = 0

with open("citystate.in", "r") as fin:
    n = int(fin.readline().strip())
    for i in range(n):
        city, state = fin.readline().strip().split()
        cities.append(city[:2])
        states.append(state)

        pairs[city[:2] + state] = state

        
for (key, value) in pairs.items():
    if value + key[:2] in pairs and key[:2] != value:
        count += 1


with open("citystate.out", "w") as fout:
    # fout.write(str(count//2) + "\n")
    fout.write(str(ceil(count/2)) + "\n")