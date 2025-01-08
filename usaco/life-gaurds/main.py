sim = [0] * 1000
n = 0
lifegaurds = []

with open("lifeguards.in", "r") as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(int, f.readline().split())
        lifegaurds.append((a, b))
        for j in range(a-1, b-1):
            sim[j] += 1

anws = 0

for i in range(n):
    copy = sim.copy()

    for j in range(lifegaurds[i][0]-1, lifegaurds[i][1]-1):
        copy[j] -= 1

    unitsCovered = 0

    for j in range(1000):
        if copy[j] > 0:
            unitsCovered += 1

    anws = max(anws, unitsCovered)
        
with open("lifeguards.out", "w") as f:
    f.write(str(anws))
    f.write("\n")