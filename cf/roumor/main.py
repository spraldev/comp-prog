import sys


N, M = map(int, input().split())
A = list(map(int, input().split()))

adj = {i: [] for i in range(N)}

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

def bfs(adj, visited, start, comp):
    q = [start]
    visited[start] = True

    while q:
        node = q.pop(0)
        comp.append(node)

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)


def connected_components(adj):
    visited = [False] * N
    alr_spread = []
    cost = 0

    for node in range(N):
        if not visited[node]:
            comp = []
            bfs(adj, visited, node, comp)
            cost += min([A[node] for node in comp])
            alr_spread += [comp]

    return alr_spread, cost


alr_spread, cost = connected_components(adj)
nodes_in_components = set([node for comp in alr_spread for node in comp])

for i in range(N):
    if i not in nodes_in_components:
        cost += A[i]
    
print(cost)