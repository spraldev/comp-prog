N = 0
dirs = []

with open('mowing.in', "r") as f:
    N = int(f.readline().strip())
    
    for i in range(N):
        line = f.readline().strip().split()
        dirs.append((line[0], int(line[1])))


pos = (0, 0)
t = 0

visited = {}
visited[pos] = 0

anws = float('inf')

for i in range(N):

    delta = (0, 0)
    if dirs[i][0] == 'N':
        delta = (0, 1)
    elif dirs[i][0] == 'S':
        delta = (0, -1)
    elif dirs[i][0] == 'E':
        delta = (1, 0)
    elif dirs[i][0] == 'W':
        delta = (-1, 0)
        
    for j in range(dirs[i][1]):
        t += 1



        pos = (pos[0] + delta[0], pos[1] + delta[1])

        if pos in visited:
            anws = min(anws, t - visited[pos])
            continue
        visited[pos] = t

with open('mowing.out', "w") as f:
    f.write(str(anws if anws != float("inf") else -1) + "\n")   

        