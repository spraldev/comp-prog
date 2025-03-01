T = int(input())

def solve():
    N, A, B = map(int, input().split())
    grid = [list(input()) for _ in range(N)]
    

    if A == 0 and B == 0:
        black_count = 0
        gray_count = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 'B':
                    black_count += 1
                elif grid[i][j] == 'G':
                    gray_count += 1
        return black_count + gray_count
    
    count = 0
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'W':
                continue

            if i - B < 0 or j - A < 0:
                if grid[i][j] == 'G':
                    count += 1
                continue

            if i + B >= N or j + A >= N:
                if grid[i][j] == 'G' and (grid[i-B][j-A] == 'B' or grid[i-B][j-A] == 'G'):
                    count += 1
                continue

            if grid[i][j] == 'B':
                count += 1
                # check if it is bad
                if grid[i+B][j+A] == 'W'and grid[i-B][j-A] == 'W':
                    return -1

            if grid[i][j] == 'G':
                if grid[i-B][j-A] == 'B' or grid[i-B][j-A] == 'G':
                    continue
                if grid[i+B][j+A] == 'B':
                    count += 1
                    continue
                if grid[i-B][j-A] == "W":
                    count += 1
                    continue

                # check if it is bad

                if grid[i+B][j+A] == 'W'and grid[i-B][j-A] == 'W':
                    return -1


            


    return count

for _ in range(T):
    print(solve())
