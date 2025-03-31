import sys

sys.stdin = open("socdist.in", "r")
sys.stdout = open("socdist.out", "w")

N, M = map(int, input().split())
intervals = sorted([list(map(int, input().split())) for _ in range(M)])


def check(D):
    cur_pos = intervals[0][0] 
    cows_left = N - 1 
    i = 0
    
    while cows_left > 0:
        cur_pos += D
        
        while i < M and intervals[i][1] < cur_pos:
            i += 1
            
        if i >= M:
            return False
            
        if cur_pos < intervals[i][0]:
            cur_pos = intervals[i][0]
            
        cows_left -= 1
        
    return True
        
lo = 0
hi = 10**18
anws = 0

while lo <= hi:
    mid = lo + (hi - lo) // 2

    if check(mid):
        anws = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(anws)