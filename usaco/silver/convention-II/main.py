import heapq

# Read from file instead of stdin
cows = []
with open("convention2.in") as read:
    N = int(read.readline())
    for i in range(N):
        arrival, duration = map(int, read.readline().split())
        cows.append((i, arrival, duration))  # (seniority, arrival, duration)

# Sort by arrival time
cows.sort(key=lambda x: x[1])

time = 0
curr = 0
anws = 0
waiting = []
heapq.heapify(waiting)

while curr < len(cows) or waiting:
    if curr < len(cows) and cows[curr][1] <= time:
        heapq.heappush(waiting, cows[curr])
        curr += 1
    elif not waiting:
        time = cows[curr][1]
        heapq.heappush(waiting, cows[curr])
        curr += 1
    else:
        next_cow = heapq.heappop(waiting)
        anws = max(anws, time - next_cow[1])
        time += next_cow[2]

# Write to file instead of stdout
print(anws, file=open("convention2.out", "w"))
