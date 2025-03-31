from collections import deque
import sys

sys.stdin = open("mootube.in", "r")
sys.stdout = open("mootube.out", "w")

# read the input

N, Q = map(int, input().split())

adj = {i: [] for i in range(1, N+1)}

relHashMap = {}

for i in range(N-1):
    p, q, r = map(int, input().split())
    adj[p].append(q)
    adj[q].append(p)
    relHashMap[(p, q)] = r
    relHashMap[(q, p)] = r

# solve with bfs

def solve(k, v):
    ret = 0
    vis = [False] * (N+1)

    q = deque([v])

    while q:
        node = q.popleft()
        vis[node] = True
        for child in adj[node]:
            if not vis[child] and relHashMap[(node, child)] >= k:
                ret += 1
                q.append(child)

            # otherwise, we dont need to keep searching on this path


    return ret

for _ in range(Q):
    k, v = map(int, input().split())
    print(solve(k, v))
