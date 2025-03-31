from collections import deque
import sys

sys.stdin = open('milkvisits.in', 'r')
sys.stdout = open('milkvisits.out', 'w')
sys.setrecursionlimit(200006) # 10^5

N, M = map(int, input().split())

GorHHashMap = {}
GorH = input()

for i in range(N):
    GorHHashMap[i + 1] = GorH[i]

adj = {i: [] for i in range(1, N + 1)}

for _ in range(N-1):
    imp = list(map(int, input().split()))
    adj[imp[0]] = adj.get(imp[0], []) + [imp[1]]
    adj[imp[1]] = adj.get(imp[1], []) + [imp[0]]

friends = []

for _ in range(M):
    imp = input().split()
    friends.append((int(imp[0]), int(imp[1]), imp[2]))

# seen2d = [[set() for _ in range(N + 1)] for _ in range(N + 1)]


def dfs(current_node, target, path, seen, GorH):
    path.append(current_node)

    if current_node == target:
        for node in path:
            seen.add(GorHHashMap[node])
        return True
    
    visited[current_node] = True

    for neighbor in adj[current_node]:
        if not visited[neighbor]:
            if dfs(neighbor, target, path, seen):
                return True
    
    path.pop()
    return False


for friend in friends:
    visited = [False] * (N + 1)

    path = [friend[0]]
    seen = set()

    dfs(friend[0], friend[1], path, seen, friend[2])

    if friend[2] in seen:
        print(1, end="")
    else:
        print(0, end="")



print()