cows = ""


with open("circlecross.in", "r") as f:
    cows = f.readline().strip()

crosses = 0

for i in range(len(cows)):
    for j in range(i +1, len(cows)):
        for k in range(j + 1, len(cows)):
            for l in range(k + 1, len(cows)):
                if cows[i] == cows[k] and cows[j] == cows[l]:
                    crosses += 1

with open("circlecross.out", "w") as f:
    f.write(str(crosses) + "\n")