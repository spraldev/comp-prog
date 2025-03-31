import sys
from collections import deque


MAX_N = 100
sys.setrecursionlimit(2**30)  # pretty much disable the recurion limit

sys.stdin = open("countcross.in", "r")
sys.stdout = open("countcross.out", "w")

N, K, R = map(int, input().split())
roads_hashmap = {}
grid = [[False] * N for _ in range(N)]

for _ in range(R):
    a, b, c, d = map(int, input().split())

    roads_hashmap[(a-1, b-1)] = (c-1, d-1)

for _ in range(K):
    x, y = map(int, input().split())
    grid[x-1][y-1] = True


visited = [[False for _ in range(N)] for _ in range(N)]
connected_components = []

def floodfill(r: int, c: int, color: bool, current_component: list):
	global ans

	if (
		(r < 0 or r >= N or c < 0 or c >= N)  
		or grid[r][c] != color  
		or visited[r][c]
		or (r, c) not in roads_hashmap
	):
		return

	visited[r][c] = True  
	current_component.append((r, c))

	# recursively call flood fill for neighboring squares
	floodfill(r, c + 1, color, current_component)
	floodfill(r, c - 1, color, current_component)
	floodfill(r - 1, c, color, current_component)
	floodfill(r + 1, c, color, current_component)


for i in range(N):
    for j in range(N):
        if grid[i][j] and not visited[i][j]:
            current_component = []
            floodfill(i, j, True, current_component)
            connected_components.append(current_component)


# do a bfs each component
anws=0

for component in connected_components:
    anws += len(component)**2
    



print(anws)