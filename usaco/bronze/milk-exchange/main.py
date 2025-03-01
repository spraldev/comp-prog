N, M = map(int, input().split())
cow_passings = list(input())
limits = [int(x) for x in input().split()]
cows = [i for i in limits]
 
for t in range(M):
    for i in range(N):
        if cows[i] > 0:
            cows[i] -= 1
            cows[(i + (1 if cow_passings[i] == 'R' else -1) + N) % N] += 1
    for i in range(N):
        cows[i] = min(cows[i], limits[i])
 
print(sum(cows))