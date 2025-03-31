N, U = map(int, input().split())
canvas = [list(input().strip()) for _ in range(N)]
half = N // 2

groups = [[0] * half for _ in range(half)]
global_cost = 0

def group_cost(cnt):
    return min(cnt, 4 - cnt)


for i in range(half):
    for j in range(half):
        cnt = 0
        if canvas[i][j] == '#': cnt += 1
        if canvas[i][N-1-j] == '#': cnt += 1
        if canvas[N-1-i][j] == '#': cnt += 1
        if canvas[N-1-i][N-1-j] == '#': cnt += 1
        groups[i][j] = cnt
        global_cost += group_cost(cnt)

print(global_cost)

def update_cell(r, c):
    global global_cost
    gi = min(r, N - 1 - r)
    gj = min(c, N - 1 - c)
    old_cost = group_cost(groups[gi][gj])
    if canvas[r][c] == '#':
        groups[gi][gj] -= 1
    else:
        groups[gi][gj] += 1
    canvas[r][c] = '#' if canvas[r][c] == '.' else '.'
    new_cost = group_cost(groups[gi][gj])
    global_cost = global_cost - old_cost + new_cost

for _ in range(U):
    r, c = map(int, input().split())
    update_cell(r - 1, c - 1)
    print(global_cost)
