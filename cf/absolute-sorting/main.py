for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    mn = 0
    mx = 10**9
    
    for i in range(n-1):
        x = arr[i]
        y = arr[i+1]
        midL = (x + y) // 2
        midR = (x + y + 1) // 2
        
        if x < y:
            mx = min(mx, midL)
        if x > y:
            mn = max(mn, midR)
    
    print(mn if mn <= mx else -1)