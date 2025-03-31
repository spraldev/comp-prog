import sys

sys.stdin = open('perimeter.in', 'r')
sys.stdout = open('perimeter.out', 'w')

sys.setrecursionlimit(2**30)

# read input


N = int(input())
grid = [list(input()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
anws = []


# floodfill function

def floodfill(r: int, c: int, color: int):
	global curr_area
	global param

	if (
		(r < 0 or r >= N or c < 0 or c >= N) 
		or grid[r][c] != color 
		or visited[r][c]
	):
		return
	
	p_count = 0
	
	if r >= N-1 or grid[r+1][c] == '.':
		p_count += 1
		
	if r <= 0 or grid[r-1][c] == '.':
		p_count += 1
		
	if c >= N-1 or grid[r][c+1] == '.':
		p_count += 1
		
	if c <= 0 or grid[r][c-1] == '.':
		p_count += 1
		
	param += p_count

	visited[r][c] = True 
	curr_area += 1 
	
	floodfill(r, c + 1, color)
	floodfill(r, c - 1, color)
	floodfill(r - 1, c, color)
	floodfill(r + 1, c, color)
	

# main loop 

for i in range(N):
	for j in range(N):
		if not visited[i][j] and grid[i][j] == "#":
			param = 0
			curr_area = 0
			floodfill(i, j, "#")
			anws.append((curr_area, param))


# sorting 


anws.sort(key=lambda x: (-x[0], x[1]))

print(anws[0][0], anws[0][1])