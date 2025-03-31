import sys

sys.setrecursionlimit(10**6)

sys.stdin = open("mooyomooyo.in", "r")
sys.stdout = open("mooyomooyo.out", "w")

N, K = map(int, input().split())
arr = [[int(x) for x in list(input().strip())] for _ in range(N)]
M = len(arr[0])

def render(arr):
    for row in arr:
        print(''.join(map(str, row)))

def gravity(board):
    new_board = [row[:] for row in board]
    for j in range(M):
        cur_line = []
        zero_cout = 0
        for i in range(N):
            if new_board[i][j] == 0:
                zero_cout += 1
            else:
                cur_line.append(new_board[i][j])
        for i in range(zero_cout):
            cur_line.insert(0, 0)
        for i in range(N):
            new_board[i][j] = cur_line[i]
    return new_board

visited = [[False for _ in range(M)] for _ in range(N)]
curr_size = 0

def floodfill(r: int, c: int, color: int, copy):
    global curr_size
    if (r < 0 or r >= N or c < 0 or c >= M or arr[r][c] != color or visited[r][c]):
        return

    visited[r][c] = True
    curr_size += 1
    copy[r][c] = 0  

    floodfill(r, c + 1, color, copy)
    floodfill(r, c - 1, color, copy)
    floodfill(r - 1, c, color, copy)
    floodfill(r + 1, c, color, copy)

while True:
    p = False

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and not visited[i][j]:
                curr_size = 0
                copy = [row[:] for row in arr]
                floodfill(i, j, arr[i][j], copy)
                if curr_size >= K:
                    arr = copy
                    p = True

    visited = [[False for _ in range(M)] for _ in range(N)]
    arr = gravity(arr)
                
    if not p:
        break

render(arr)
