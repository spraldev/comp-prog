from collections import deque
import sys

sys.stdin = open("closing.in", "r")
sys.stdout = open("closing.out", "w")


N, M = map(int, input().split())
adj = {i: [] for i in range(1, N+1)}

for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)



def remove_node(node):
    cop = adj[node].copy()
    adj[node] = []

    for neighbor in cop:
        adj[neighbor].remove(node)

closed_nodes = set()
visited = [False] * (N + 1)

Start = None

for i in range(1, N + 1):
    if i not in closed_nodes:
        Start = i
        break

if i == None:
    print("YES")
else:
	q = deque([i])

	while q:
		node = q.popleft()
		visited[node] = True
		for neighbor in adj[node]:
			if not visited[neighbor]:
				q.append(neighbor)
p = False


for i in range(1, N + 1):
    if not visited[i] and i not in closed_nodes:
        p = True
        break

print("YES" if not p else "NO")



for _ in range(N-1):
    num = int(input())
    visited = [False] * (N + 1)

    closed_nodes.add(num)
    remove_node(num)

    Start = None

    for i in range(1, N + 1):
        if i not in closed_nodes:
            Start = i
            break

    if i == None:
        print("YES")
    else:
        q = deque([i])

        while q:
            node = q.popleft()
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    q.append(neighbor)
    p = False


    for i in range(1, N + 1):
        if not visited[i] and i not in closed_nodes:
            p = True
            break

    print("YES" if not p else "NO")