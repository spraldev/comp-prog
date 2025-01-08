#import bisect

T = int(input())

def countGreater(arr, n, k):
    l = 0
    r = n - 1
 
    leftMax = n

    while (l <= r):
        m = int(l + (r - l) / 2)
 
        if (arr[m] > k):
            leftMax = m
            r = m - 1
 
        else:
            l = m + 1
 
    return (n - leftMax)


def solve(N, heights, growths, M):
    days = 0

    passT = True

    for i in range(N):
        if countGreater(sorted(heights), N, heights[i]) != M[i]:
            passT = False
            break
    
    if passT:
        print(days)
        return

    if len(set(heights)) == 1 or len(set(growths)) == 1:
        print(-1)
        return

    while True:
        heights = [a + b for a, b in zip(heights, growths)]


        passT = True

        for i, height in enumerate(heights):
            if countGreater(sorted(heights), N, height) != M[i]:
                passT = False
                break

        days += 1
        
        if passT:
            print(days)
            return
        

            
    
for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    growths = list(map(int, input().split()))
    
    M = list(map(int, input().split()))
    
    solve(N, heights, growths, M)