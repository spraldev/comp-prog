from itertools import combinations

def inv(e):
    return "D" if e == "R" else "R"



for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    def f(pos, dir_, num):

        if num > K:
            return 0

        if pos == (N-1, N-1):
            return 1
        
        if pos[0] >= N or pos[1] >= N:
            return 0
        
        if arr[pos[0]][pos[1]] == "H":
            return 0
        
        
        
    

        if dir_ == "R":
            return f((pos[0], pos[1] + 1), "R", num) + f((pos[0] + 1, pos[1]), "D", num + 1)
        else:
            
            return f((pos[0] + 1, pos[1]), "D", num) + f((pos[0], pos[1] + 1), "R", num + 1)
    
    print(f((0,1), "R", 0) + f((1,0), "D", 0))
    

        
