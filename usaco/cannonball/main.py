N, S = list(map(int, input().split()))
arr = []
K = 1

for i in range(N):
    inp = tuple(map(int, input().split()))
    arr.append(inp if inp[0] == 0 else (inp[0], inp[1], False))

S -= 1
count = 0
daysWithout = 0


while True:
    passed = False

    for i in range(S, N):
        if arr[i][0] == 1 and arr[i][2] == False:
            passed = True
            break

    if not passed:
        break
    
    sqr = arr[S]


    if sqr[0] == 1:
        
        if abs(K) >= arr[S][1] and not arr[S][2]:
            count += 1
            arr[S] = (arr[S][0], arr[S][1], True)
            daysWithout = 0
        else:
            daysWithout += 1
        
        
        
        if S+K > N-1 or S+K < 0:
            break

        S += K
    else:
        newVar = arr[S][1] + abs(K)
        if K > 0:
            K = -newVar
        else:
            K = newVar

        if S+K > N-1 or S+K < 0:
            break

        S += K
        daysWithout += 1

    if daysWithout > 10**6:
        break

    

print(count)