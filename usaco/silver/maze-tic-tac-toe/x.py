N = int(input())

arr = []

for _ in range(N):
    line = input()
    arr.append([line[i:i+3] for i in range(0, len(line), 3)]
)
    
board = [[cell if cell != "BBB" else "..." for cell in row] for row in arr]

possible_winning_states = set()
visited = [[False for _ in range(N)] for _ in range(N)]


def get_all_valid_diagonals_and_adjacent(board, i, j):
    diagnoals = [[(i-1, j-1), (i-2, j-2)], [(i-1, j+1), (i-2, j+2)], [(i+1, j-1), (i+2, j-2)], [(i+1, j+1), (i+2, j+2)]]
    adjacent = [[(i-1, j), (i-2, j)], [(i+1, j), (i+2, j)], [(i, j-1), (i, j-2)], [(i, j+1), (i, j+2)]]
    valid_diags = []
    for diag in diagnoals:
        if 0 <= diag[0][0] < 3 and 0 <= diag[0][1] < 3 and 0 <= diag[1][0] < 3 and 0 <= diag[1][1] < 3:
            valid_diags.append(diag)
    valid_adj = []
    for adj in adjacent:
        if 0 <= adj[0][0] < 3 and 0 <= adj[0][1] < 3 and 0 <= adj[1][0] < 3 and 0 <= adj[1][1] < 3:
            valid_adj.append(adj)
    return valid_diags, valid_adj

def flood_fill(x, y, board, tic_tac_toe):
    if x < 0 or x >= N or y < 0 or y >= N:
        return
    if visited[x][y]:
        return
    
    if board[x][y] == "###":
        return
    
    visited[x][y] = True
    
    if board[x][y] == "...":
        for l in range(3):
            for m in range(3):
                new_tic_tac_toe = [row[:] for row in tic_tac_toe]
                if new_tic_tac_toe[l][m] != ".":
                    continue
                new_tic_tac_toe[l][m] = "M"
                for i in range(3):
                    for j in range(3):
                        valid_diags, valid_adj = get_all_valid_diagonals_and_adjacent(board, i, j)
                        for diag in valid_diags:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[diag[0][0]][diag[0][1]] == "O" and new_tic_tac_toe[diag[1][0]][diag[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                        for adj in valid_adj:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[adj[0][0]][adj[0][1]] == "O" and new_tic_tac_toe[adj[1][0]][adj[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                        flood_fill(x + 1, y, board, new_tic_tac_toe)
                        flood_fill(x - 1, y, board, new_tic_tac_toe)
                        flood_fill(x, y + 1, board, new_tic_tac_toe)
                        flood_fill(x, y - 1, board, new_tic_tac_toe)
                
                new_tic_tac_toe[l][m] = "O"
                
                for i in range(3):
                    for j in range(3):
                        valid_diags, valid_adj = get_all_valid_diagonals_and_adjacent(board, i, j)
                        for diag in valid_diags:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[diag[0][0]][diag[0][1]] == "O" and new_tic_tac_toe[diag[1][0]][diag[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                        for adj in valid_adj:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[adj[0][0]][adj[0][1]] == "O" and new_tic_tac_toe[adj[1][0]][adj[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                        flood_fill(x + 1, y, board, new_tic_tac_toe)
                        flood_fill(x - 1, y, board, new_tic_tac_toe)
                        flood_fill(x, y + 1, board, new_tic_tac_toe)
                        flood_fill(x, y - 1, board, new_tic_tac_toe)
                
                new_tic_tac_toe[l][m] = "."
                
                for i in range(3):
                    for j in range(3):
                        valid_diags, valid_adj = get_all_valid_diagonals_and_adjacent(board, i, j)
                        for diag in valid_diags:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[diag[0][0]][diag[0][1]] == "O" and new_tic_tac_toe[diag[1][0]][diag[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                        for adj in valid_adj:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[adj[0][0]][adj[0][1]] == "O" and new_tic_tac_toe[adj[1][0]][adj[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                    flood_fill(x + 1, y, board, new_tic_tac_toe)
                    flood_fill(x - 1, y, board, new_tic_tac_toe)
                    flood_fill(x, y + 1, board, new_tic_tac_toe)
                    flood_fill(x, y - 1, board, new_tic_tac_toe)
        
        for i in range(3):
            for j in range(3):
                valid_diags, valid_adj = get_all_valid_diagonals_and_adjacent(board, i, j)
                for diag in valid_diags:
                    if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[diag[0][0]][diag[0][1]] == "O" and new_tic_tac_toe[diag[1][0]][diag[1][1]] == "O"):
                        possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                for adj in valid_adj:
                    if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[adj[0][0]][adj[0][1]] == "O" and new_tic_tac_toe[adj[1][0]][adj[1][1]] == "O"):
                        possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                flood_fill(x + 1, y, board, new_tic_tac_toe)
                flood_fill(x - 1, y, board, new_tic_tac_toe)
                flood_fill(x, y + 1, board, new_tic_tac_toe)
                flood_fill(x, y - 1, board, new_tic_tac_toe)
    else:
        tic_tac_toe = [["."] * 3 for _ in range(3)]
        if tic_tac_toe[int(board[x][y][1]) - 1][int(board[x][y][2]) - 1] == ".":
            tic_tac_toe[int(board[x][y][1]) - 1][int(board[x][y][2]) - 1] = board[x][y][0]
        for l in range(3):
            for m in range(3):
                new_tic_tac_toe = [row[:] for row in tic_tac_toe]
                if new_tic_tac_toe[l][m] != ".":
                    continue
                new_tic_tac_toe[l][m] = "M"
                for i in range(3):
                    for j in range(3):
                        valid_diags, valid_adj = get_all_valid_diagonals_and_adjacent(board, i, j)
                        for diag in valid_diags:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[diag[0][0]][diag[0][1]] == "O" and new_tic_tac_toe[diag[1][0]][diag[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                        for adj in valid_adj:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[adj[0][0]][adj[0][1]] == "O" and new_tic_tac_toe[adj[1][0]][adj[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                        flood_fill(x + 1, y, board, new_tic_tac_toe)
                        flood_fill(x - 1, y, board, new_tic_tac_toe)
                        flood_fill(x, y + 1, board, new_tic_tac_toe)
                        flood_fill(x, y - 1, board, new_tic_tac_toe)
                new_tic_tac_toe[l][m] = "O"
                for i in range(3):
                    for j in range(3):
                        valid_diags, valid_adj = get_all_valid_diagonals_and_adjacent(board, i, j)
                        for diag in valid_diags:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[diag[0][0]][diag[0][1]] == "O" and new_tic_tac_toe[diag[1][0]][diag[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                        for adj in valid_adj:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[adj[0][0]][adj[0][1]] == "O" and new_tic_tac_toe[adj[1][0]][adj[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                        flood_fill(x + 1, y, board, new_tic_tac_toe)
                        flood_fill(x - 1, y, board, new_tic_tac_toe)
                        flood_fill(x, y + 1, board, new_tic_tac_toe)
                        flood_fill(x, y - 1, board, new_tic_tac_toe)
                new_tic_tac_toe[l][m] = "."
                for i in range(3):
                    for j in range(3):
                        valid_diags, valid_adj = get_all_valid_diagonals_and_adjacent(board, i, j)
                        for diag in valid_diags:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[diag[0][0]][diag[0][1]] == "O" and new_tic_tac_toe[diag[1][0]][diag[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                        for adj in valid_adj:
                            if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[adj[0][0]][adj[0][1]] == "O" and new_tic_tac_toe[adj[1][0]][adj[1][1]] == "O"):
                                possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                    flood_fill(x + 1, y, board, new_tic_tac_toe)
                    flood_fill(x - 1, y, board, new_tic_tac_toe)
                    flood_fill(x, y + 1, board, new_tic_tac_toe)
                    flood_fill(x, y - 1, board, new_tic_tac_toe)
        for i in range(3):
            for j in range(3):
                valid_diags, valid_adj = get_all_valid_diagonals_and_adjacent(board, i, j)
                for diag in valid_diags:
                    if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[diag[0][0]][diag[0][1]] == "O" and new_tic_tac_toe[diag[1][0]][diag[1][1]] == "O"):
                        possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                for adj in valid_adj:
                    if new_tic_tac_toe[i][j] == "M" and (new_tic_tac_toe[adj[0][0]][adj[0][1]] == "O" and new_tic_tac_toe[adj[1][0]][adj[1][1]] == "O"):
                        possible_winning_states.add(tuple(tuple(x) for x in new_tic_tac_toe))
                flood_fill(x + 1, y, board, new_tic_tac_toe)
                flood_fill(x - 1, y, board, new_tic_tac_toe)
                flood_fill(x, y + 1, board, new_tic_tac_toe)
                flood_fill(x, y - 1, board, new_tic_tac_toe)

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            flood_fill(i, j, board, [["."] * 3 for _ in range(3)])

print(len(possible_winning_states))
