n = 0

cities = []
states = []

pairs = {}

with open("citystate.in", "r") as fin:
    n = int(fin.readline().strip())
    for i in range(n):
        city, state = fin.readline().strip().split()
        cities.append(city[:2])
        states.append(state)


        if city[:2] + state not in pairs:
            pairs[city[:2] + state] = 1
        else:
            pairs[city[:2] + state] += 1

print(pairs)
count = 0;

def reverse_by_pairs(string):
    reversed_string = ""
    for i in range(len(string) - 1, -1, -2):
        reversed_string += string[i-1:i+1]
    return reversed_string

for key in pairs:

    if(reverse_by_pairs(key) in pairs):
        count += pairs[key] * pairs[reverse_by_pairs(key)]





        

with open("citystate.out", "w") as fout:
    fout.write(str(count//2) + "\n")