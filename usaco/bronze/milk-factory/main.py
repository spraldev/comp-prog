from collections import deque
import sys

sys.stdin = open('factory.in', 'r')
sys.stdout = open('factory.out', 'w')


N = int(input())

adj = {i: [] for i in range(1, N + 1)}

for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)

for candidate in range(1, N+1):
    res = []
    
    for j in range(1, N+1):
        visited = [False] * (N+1)
        q = deque([j])
        
        while q:
            node = q.popleft()
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    q.append(neighbor)
                    
        res.append(visited[candidate])
    
    if all(res):
        print(candidate)
        exit()

print(-1)
