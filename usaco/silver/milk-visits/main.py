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

adjG = {i: [] for i in range(1, N + 1)}
adjH = {i: [] for i in range(1, N + 1)}

for _ in range(N-1):
    imp = list(map(int, input().split()))

    if GorHHashMap[imp[0]] == 'G' and GorHHashMap[imp[1]] == 'G':
        adjG[imp[0]] = adjG.get(imp[0], []) + [imp[1]]
        adjG[imp[1]] = adjG.get(imp[1], []) + [imp[0]]

    elif GorHHashMap[imp[0]] == 'H' and GorHHashMap[imp[1]] == 'H':
        adjH[imp[0]] = adjH.get(imp[0], []) + [imp[1]]
        adjH[imp[1]] = adjH.get(imp[1], []) + [imp[0]]

friends = []

for _ in range(M):
    imp = input().split()
    friends.append((int(imp[0]), int(imp[1]), imp[2]))


visited = [False] * (N + 1)


def mock_floodfill(curr, adj):
    visited[curr] = True
    ste.add(curr)
    for neighbor in adj[curr]:
        if not visited[neighbor]:
            mock_floodfill(neighbor, adj)
    return


visited = [False] * (N + 1)
connectedG = []
for i in range(1, N + 1):
    if GorHHashMap[i] == 'G' and not visited[i]:
        ste = set()
        mock_floodfill(i, adjG)
        connectedG.append(ste)

visited = [False] * (N + 1)
connectedH = []
for i in range(1, N + 1):
    if GorHHashMap[i] == 'H' and not visited[i]:
        ste = set()
        mock_floodfill(i, adjH)
        connectedH.append(ste)


for friend in friends:
    A, B, pref = friend
    if GorHHashMap[A] == pref or GorHHashMap[B] == pref:
        print(1, end="")
    else:
        happy = 0
        if pref == 'G':
            for comp in connectedG:
                if A in comp and B in comp:
                    happy = 1
                    break
        else:  # pref == 'H'
            for comp in connectedH:
                if A in comp and B in comp:
                    happy = 1
                    break
        print(happy, end="")

print()