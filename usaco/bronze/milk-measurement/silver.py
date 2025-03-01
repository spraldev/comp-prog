N, G = 0, 0
cows = {}
arr = []

with open("measurement.in", "r") as f:
    N, G = list(map(int, f.readline().strip().split()))
    for _ in range(N):
        line = f.readline().strip().split()

        if int(line[1]) not in cows:
            cows[int(line[1])] = G

        arr.append((int(line[0]), int(line[1]), int(line[2])))


arr.sort()
max_cow = G
anws = 0
max_indexes = []


for time, cow, change in arr:
    # cows[cow] += change
    # new_max = max(cows.values())
    # new_max_indexes = [x for x, val in cows.items() if val == new_max]

    # if sorted(new_max_indexes) != sorted(max_indexes):
    #     anws += 1
    #     max_indexes = new_max_indexes

    if change > 0:
        cows[cow] += change
        
        if cows[cow] > max_cow:
            max_cow = cows[cow]
            anws += 1
            max_indexes = [c for c, val in cows.items() if val == max_cow]
        elif cows[cow] == max_cow:
            max_indexes.append(cow)
            anws += 1
        
    else:
        cows[cow] += change
        old_max = max_cow
        max_cow = max(cows.values())

        if cows[cow] == max_cow:
            if max_cow > old_max:
                anws += 1
                max_indexes = [c for c, val in cows.items() if val == max_cow]
            elif max_cow == old_max:
                max_indexes.append(cow)
                anws += 1
        else:
            if cow in max_indexes:
                max_indexes.remove(cow)
                anws += 1
            if max_cow < old_max:
                anws += 1
                max_indexes = [c for c, val in cows.items() if val == max_cow]
            else:
                anws += 1

                
with open("measurement.out", "w") as f:
    f.write(str(anws) + "\n")
        

