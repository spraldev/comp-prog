cow_names = []
cow_pairs = []

result = []


with open("lineup.in", "r") as f:
    n = int(f.readline().strip())
    for i in range(n):
        line = f.readline().strip().split()
        cow_names.append(line[0])
        cow_names.append(line[5])
        cow_pairs.append((line[0], line[5]))

cow_names.sort()

cow_pairs.sort()

#print(cow_pairs)

def recursive(name=cow_names[0]):
    if(len(result) == len(cow_names)):
        return
    
    clone = cow_pairs.copy()
    
    res = [tup for tup in cow_pairs if name in tup]
    if(not res):
        return print("hi")

    result.append(name)

    if res[0] == name:
        result.append(res[0][1])
        recursive(res[0][1])
    else:
        result.append(res[0][0])
        recursive(res[0][0])


    cow_pairs.pop(cow_pairs.index(res)) 

recursive()
