from collections import deque
import sys

sys.stdin = open("moocast.in", "r")
sys.stdout = open("moocast.out", "w")

def squared_distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

N = int(input())
cows = []
for _ in range(N):
    X, Y, P = map(int, input().split())
    cows.append((X, Y, P))


adj = {i: [] for i in range(N)}
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if squared_distance(cows[i][:2], cows[j][:2]) <= cows[i][2]**2:
            adj[i].append(j)

anws = 0  
for i in range(N): 
    q = deque([i])  
    visited = [False] * N
    visited[i] = True 
    cnt = 1  
      
    while q:
        node = q.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                cnt += 1

    anws = max(anws, cnt)

print(anws) 