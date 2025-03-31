from collections import deque
import sys

sys.stdin = open("moocast.in", "r")
sys.stdout = open("moocast.out", "w")

N = int(input())
cows = []
for _ in range(N):
    X, Y = map(int, input().split())
    cows.append((X, Y))

def do_stuff(P):
    def squared_distance(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    adj = {i: [] for i in range(N)}
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if squared_distance(cows[i][:2], cows[j][:2]) <= P:
                adj[i].append(j)

    anws = 0  
    p = False
    for i in range(N): 
        q = deque([i])  
        visited = [False] * N
        visited[i] = True 
        
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

        if all(visited):
            p = True
            break

    return p


lo = 0
hi = 10**9

anws = 0

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if do_stuff(mid):
        anws = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(anws)