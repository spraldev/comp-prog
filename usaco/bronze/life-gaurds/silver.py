n = 0
lifegaurds = []

with open("lifeguards.in", "r") as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(int, f.readline().split())
        lifegaurds.append((a, b))


lifegaurds.sort()
totalTime = 0
maxTime = 0

for i in range(n):
    if i == 0:
        totalTime = lifegaurds[i][1] - lifegaurds[i][0]
    else:
        totalTime += lifegaurds[i][1] - max(lifegaurds[i-1][1], lifegaurds[i][0])
print(totalTime)

for i in range(n):
    if i == n-1:
        leftOverlap = max(0, lifegaurds[i-1][1] - lifegaurds[i][0])
        maxTime = max(maxTime, totalTime - leftOverlap)
    elif i == 0:
        rightOverlap = max(0, lifegaurds[i][1] - lifegaurds[i+1][0])
        maxTime = max(maxTime, totalTime - rightOverlap)
    else:
        # calculate overlap

        leftOverlap = max(0, lifegaurds[i-1][1] - lifegaurds[i][0])
        rightOverlap = max(0, lifegaurds[i][1] - lifegaurds[i+1][0])

        maxTime = max(maxTime, totalTime - leftOverlap - rightOverlap)

with open("lifeguards.out", "w") as f:
    f.write(str(maxTime) + "\n")

