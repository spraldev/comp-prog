import sys

sys.stdin = open('lightson.in', 'r')
sys.stdout = open('lightson.out', 'w')

sys.setrecursionlimit(2**30)


N, M = map(int, input().split())
hashmap = {}

for i in range(M):
	imp = list(map(int, input().split()))
	hashmap[(imp[0]-1, imp[1]-1)] = hashmap.get((imp[0]-1, imp[1]-1), []) + [(imp[2]-1, imp[3]-1)]

    
on = [[False for i in range(N)] for j in range(N)]
visited = [[False for i in range(N)] for j in range(N)]
	

anws = 1

def check_connected(r: int, c: int):
    if (r-1 >= 0 and visited[r-1][c]) or \
       (c-1 >= 0 and visited[r][c-1]) or \
       (r+1 < N and visited[r+1][c]) or \
       (c+1 < N and visited[r][c+1]):
        return True
    return False

def floodfill(r: int, c: int, ):
    global anws

    if (r < 0 or r >= N or c < 0 or c >= N):
        return
    
    if not on[r][c]:
        return

    if (visited[r][c] == True):
        return
    
    if not check_connected(r, c) and (r, c) != (0, 0):
        return

    
    visited[r][c] = True
    switch = hashmap.get((r, c), [])
    
    for i in switch:
        if not on[i[0]][i[1]]:
            on[i[0]][i[1]] = True
            anws += 1
            floodfill(i[0], i[1],)
    

	
    floodfill(r, c + 1,)
    floodfill(r, c - 1,)
    floodfill(r - 1, c, )
    floodfill(r + 1, c, )

on[0][0] = True

floodfill(0, 0)

print(anws)