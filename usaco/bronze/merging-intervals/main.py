N, K = list(map(int, input().split()))
intervals = []

for _ in range(N):
    intervals.append(tuple(map(int, input().split())))

anws = len(intervals ) - 1
merges = 0


for i in range(len(intervals)):
    if i == len(intervals) - 1:
        break

    if merges >= K:
        break

    if intervals[i][1] >= intervals[i + 1][0]:
        anws -= 1
        merges += 1

print(anws)


