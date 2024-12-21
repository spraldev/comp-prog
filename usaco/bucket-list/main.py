N = 0
cows = []
sim = [0] * 100000

with open("blist.in", "r") as f:
    N = int(f.readline().strip())
    cows = [tuple(map(int, f.readline().strip().split())) for _ in range(N)]

for i in range(len(cows)):
    for j in range(cows[i][0]+1, cows[i][1]+1):
        sim[j] += cows[i][2]


with open("blist.out", "w") as f:
    f.write(f"{max(sim)}")