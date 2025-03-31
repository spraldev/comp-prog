import sys

sys.setrecursionlimit(10**6)
sys.stdin = open("multimoo.in", "r")
sys.stdout = open("multimoo.out", "w")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

order_map = {}
region = {}

# --- Modified floodfill ---
# Instead of passing a running count, return the total cell count.
def floodfill(r: int, c: int, color: int, label) -> int:
    if r < 0 or r >= N or c < 0 or c >= N or isinstance(arr[r][c], tuple) or arr[r][c] != color:
        return 0
    arr[r][c] = (color, label)
    cnt = 1
    cnt += floodfill(r + 1, c, color, label)
    cnt += floodfill(r - 1, c, color, label)
    cnt += floodfill(r, c + 1, color, label)
    cnt += floodfill(r, c - 1, color, label)
    return cnt

cow_set = set()
first_occur = {}

for i in range(N):
    for j in range(N):
        if isinstance(arr[i][j], tuple):
            continue
        color = arr[i][j]
        label = order_map.get(color, 0) + 1
        order_map[color] = label
        first_occur[(color, label)] = (i, j)
        size = floodfill(i, j, color, label)
        region[(color, label)] = size
        cow_set.add(color)

cows = list(cow_set)

graph = {}

for cow in cows:
    for i in range(1, order_map[cow] + 1):
        graph[(cow, i)] = set()

for i in range(N):
    for j in range(N):
        cur = arr[i][j]  # This is now a tuple (cow, label)
        neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for ni, nj in neighbors:
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            if arr[ni][nj] == cur:
                continue
            graph[cur].add(arr[ni][nj])
            graph[arr[ni][nj]].add(cur)

# --- Modified DFS for team regions ---
# This DFS “collects” the connected component (in comp)
# while propagating an "allowed" set (of cow IDs seen so far).
# We do not use a global visited; instead, each DFS call uses comp (the set of nodes in this component)
# and we make a new copy of the allowed set in each recursive call.
def dfs(node: tuple, cur_set: set, comp: set) -> set:
    if node in comp:
        return cur_set
    new_set = cur_set | {node[0]}  # add this node's cow ID
    if len(new_set) > 2:
        return cur_set  # do not add node if it would make more than 2 cows
    comp.add(node)
    for nb in graph[node]:
        new_set |= dfs(nb, new_set, comp)
    return new_set

# Run DFS over the region graph to compute team regions.
team_ans = 0
visited_team = set()
for cow in cows:
    for i in range(1, order_map[cow] + 1):
        node = (cow, i)
        if node in visited_team:
            continue
        comp = set()
        allowed = dfs(node, set(), comp)
        visited_team |= comp  # mark entire component as visited
        if len(allowed) == 2:
            comp_sum = sum(region[x] for x in comp)
            if comp_sum > team_ans:
                team_ans = comp_sum

# Single-cow answer: the largest region among all regions.
single_ans = max(region.values()) if region else 0

print(single_ans)
print(team_ans)
