for _ in range(int(input())):
    x, y, a = map(int, input().split())
    
    goal = a + 0.5
    
    lo = 0
    hi = 10**9
    ans = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * (x + y) >= goal:
            hi = mid - 1
        else:
            ans = mid
            lo = mid + 1


    cur = ans * (x + y)
    flag = True 
    
    while cur < goal:
        if flag:
            cur += x
        else:
            cur += y
        flag = not flag


    print("yes" if flag else "no")
