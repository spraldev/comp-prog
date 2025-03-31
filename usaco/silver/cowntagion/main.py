import sys
sys.setrecursionlimit(10**7)

N = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

days = 0

def dfs(u, parent):
    global days
    children = 0
    for v in adj[u]:
        if v == parent:
            continue
        children += 1
        dfs(v, u)
    d = 0
    while (1 << d) < children:
        d += 1
    days += d

dfs(1, 0)
days += N - 1
print(days)