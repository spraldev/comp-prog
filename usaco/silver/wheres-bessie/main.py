import sys

# sys.stdin = open('where.in', 'r')
# sys.stdout = open('where.out', 'w')

sys.setrecursionlimit(2**30)

N = int(input())

grid = [list(input()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
anws = 0

def floodfill(r: int, c: int, color: set):
	global end

	if (
		(r < 0 or r >= N or c < 0 or c >= N) 
		or visited[r][c]
	):
		return

	color.add(grid[r][c])

	
	end = (r, c)

	visited[r][c] = True 

	floodfill(r, c + 1, color)
	floodfill(r, c - 1, color)
	floodfill(r - 1, c, color)
	floodfill(r + 1, c, color)


	if len(color) == 2:
		return


cur_pcls = set()

for r in range(N):
	for c in range(N):
		if not visited[r][c]:
			start = (r, c)
			end = (r, c)

			color = set()

			floodfill(r, c, color)
			p = True

			for pcls in cur_pcls:
				if (
					(start[0] >= pcls[0][0] and start[1] >= pcls[0][1])
					and (end[0] <= pcls[1][0] and end[1] <= pcls[1][1])
				):
					p = False
					break

			if p and len(color) == 2:
				anws += 1
				cur_pcls.add((start, end))


print(anws)
