buckets = []
capactiy = []


with open ("mixmilk.in", "r") as f:
    for line in f.readlines():
        b, a = map(int, line.split())
        buckets.append(a)
        capactiy.append(b)

buc_pored = 1

for i in range(100):
    current_buc = buckets[buc_pored - 1];
    next_buc = buckets[buc_pored];

    
    if(next_buc + current_buc <= capactiy[buc_pored]):
        next_buc += current_buc
        current_buc = 0
    else:
        current_buc = current_buc  - (capactiy[buc_pored] - next_buc)
        next_buc = capactiy[buc_pored]

    buckets[buc_pored - 1] = current_buc
    buckets[buc_pored] = next_buc

    if buc_pored == 2:
        buc_pored = 0
    else:
        buc_pored += 1

    


with open("mixmilk.out", "w") as f:
    for i in range(3):
        f.write(str(buckets[i]) + "\n")

        



