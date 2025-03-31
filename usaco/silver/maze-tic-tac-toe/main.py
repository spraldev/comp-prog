import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
maze = []
start_idx = None
for i in range(N):
    line = input().strip()
    row = [line[j:j+3] for j in range(0, len(line), 3)]
    for j, cell in enumerate(row):
        if cell == "BBB":
            start_idx = i * N + j
            row[j] = "..."
    maze.append(row)
flat_maze = []
for i in range(N):
    for j in range(N):
        flat_maze.append(maze[i][j])
cell_data = [None]*(N*N)
for i in range(N):
    for j in range(N):
        idx = i * N + j
        if maze[i][j] not in ("###", "..."):
            letter = maze[i][j][0].upper()
            val = 1 if letter == 'M' else 2
            r = int(maze[i][j][1]) - 1
            c = int(maze[i][j][2]) - 1
            cell_data[idx] = (val, r * 3 + c)
neighbors = [[] for _ in range(N*N)]
for i in range(N):
    for j in range(N):
        idx = i * N + j
        if maze[i][j] == "###":
            continue
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != "###":
                neighbors[idx].append(ni * N + nj)
base = 3**9
pow3 = [3**i for i in range(9)]
win = [False] * base
for state in range(base):
    board = [0] * 9
    temp = state
    for i in range(9):
        board[i] = temp % 3
        temp //= 3
    for a, b, c in ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)):
        if board[a] == 1 and board[b] == 2 and board[c] == 2:
            win[state] = True
            break
        if board[a] == 2 and board[b] == 2 and board[c] == 1:
            win[state] = True
            break
total_states = N * N * base
visited = bytearray(total_states)
def encode(p, tic):
    return p * base + tic
q = deque()
q.append((start_idx, 0))
visited[encode(start_idx, 0)] = 1
possible = set()
while q:
    p, tic = q.popleft()
    i, j = divmod(p, N)
    new_tic = tic
    if cell_data[p] is not None:
        val, move_pos = cell_data[p]
        if (tic // pow3[move_pos]) % 3 == 0:
            new_tic = tic + val * pow3[move_pos]
    if win[new_tic]:
        possible.add(new_tic)
        continue
    for np in neighbors[p]:
        enc = np * base + new_tic
        if not visited[enc]:
            visited[enc] = 1
            q.append((np, new_tic))
sys.stdout.write(str(len(possible)))
