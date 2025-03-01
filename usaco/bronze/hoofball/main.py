N = 0
cows = []

with open('hoofball.in', "r") as f:
    N = int(f.readline())
    cows = list(map(int, f.readline().split()))

cows.sort()


def simulate(i):
    j = i
    if j == 0:
        j += 1
        return j
    elif j == N - 1:
        
        if cows[j -2] - cows[j - 1] <= cows[j - 1] - cows[j]:
            j -= 1
            return j
        else:
            return j
    else:
        if cows[j] - cows[j - 1] <= cows[j + 1] - cows[j]:
            j -= 1
            return j
        else:
            j += 1
            return j



anws = 1
i = 0


while True:
    sim = simulate(i)
    if sim < i:
        anws += 1
    
    i += 1

    if i == N - 1:
        break
    
with open('hoofball.out', "w") as f:
    f.write(str(anws))
    f.write("\n")