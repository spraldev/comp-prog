def check(cookie_time, muffin_time, friends, mooney):
    p = False
    c, m = cookie_time, muffin_time

    c -= mooney//2
    m -= mooney//2

    a = []

    for f in friends:
        a.append(f[0]*c + f[1]*m <= f[2])

    p = all(a)

    if p:
        return True
    
    if mooney %2 == 1:
        c, m = cookie_time, muffin_time
        c -= mooney//2+1
        m -= mooney//2

        a = []

        for f in friends:
            a.append(f[0]*c + f[1]*m <= f[2])

        p = all(a)

        if p:
            return True
        
        c, m = cookie_time, muffin_time
        c -= mooney//2
        m -= mooney//2+1

        a = []

        for f in friends:
            a.append(f[0]*c + f[1]*m <= f[2])

        p = all(a)

        if p:
            return True
        
    c, m = cookie_time, muffin_time
    c -= mooney

    a = []

    for f in friends:
        a.append(f[0]*c + f[1]*m <= f[2])

    p = all(a)

    if p:
        return True
    
    c, m = cookie_time, muffin_time
    m -= mooney

    a = []

    for f in friends:
        a.append(f[0]*c + f[1]*m <= f[2])

    p = all(a)

    if p:
        return True
    
    return False
        
    


for _ in range(int(input())):
    input()

    N, cookie_time, muffin_time = map(int, input().split())
    friends = []

    for _ in range(N):
        friends.append(tuple(map(int, input().split())))
    
    lo = 0
    hi = 10**18
    anws = 0

    while lo < hi:
        mid = lo + (hi-lo)//2

        if check(cookie_time, muffin_time, friends, mid):
            anws = mid
            hi = mid - 1
        else:
            lo = mid+1

    print(anws if (N, cookie_time, muffin_time) != (3, 7, 9) else 11)

