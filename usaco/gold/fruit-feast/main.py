import sys
from collections import deque


sys.setrecursionlimit(10**6)
sys.stdin = open("feast.in", "r")
sys.stdout = open("feast.out", "w")

cap, lemon, orange = map(int, input().split())
ans = 0 

def dfs( cur, has_eaten):
    global ans
    if cur <= cap:
        ans = max(ans, cur)
    else:
        return
    
    if has_eaten:
        dfs(cur + lemon, True)
        dfs(cur + orange, True)
    else:
        dfs(cur // 2, True)
        dfs(cur + lemon, False)
        dfs(cur + orange, False)

def bfs():
    global ans

    q = deque([(0, False)])
    visited = set()
    visited.add((0, False))

    while q:
        latest = q.popleft()

        if latest[0] <= cap:
            ans = max(ans, latest[0])
        else:
            continue

        if latest[1]:
            if (latest[0] + lemon, True) not in visited:
                q.append((latest[0] + lemon, True))
                visited.add((latest[0] + lemon, True))
            if (latest[0] + orange, True) not in visited:
                q.append((latest[0] + orange, True))
                visited.add((latest[0] + orange, True))
        else:
            if (latest[0] // 2, True) not in visited:
                q.append((latest[0] // 2, True))
                visited.add((latest[0] // 2, True))
            if (latest[0] + lemon, False) not in visited:
                q.append((latest[0] + lemon, False))
                visited.add((latest[0] + lemon, False))
            if (latest[0] + orange, False) not in visited:
                q.append((latest[0] + orange, False))
                visited.add((latest[0] + orange, False))



bfs()
print(ans)