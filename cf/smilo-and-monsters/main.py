def finish(m, c):
    if m < c:
        return m
    X = m - c
    if X % 2 == 0:
        return min(m, X // 2 + 1)
    else:
        return min(m, (X - 1) // 2 + 2)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    ans = 0      # total number of moves (attacks)
    cur = 0      # current combo value
    i, j = 0, n - 1
    

    while i < j:
        if cur + a[i] < a[j]:
            cur += a[i]
            ans += a[i]
            i += 1
        elif cur + a[i] == a[j]:
            cur += a[i]
            ans += a[i]
            ans += 1
            cur = 0
            i += 1
            j -= 1
        else:
            needed = a[j] - cur
            if needed > 0:
                ans += needed
                a[i] -= needed
                cur += needed
            ans += 1
            cur = 0
            j -= 1
            if a[i] == 0:
                i += 1


    if i == j:
        ans += finish(a[i], cur)
    
    print(ans)
