N, M = map(int, input().split())
cows = list(map(int, input().split()))
candy_canes = list(map(int, input().split()))


for i in range(M):
    cane = candy_canes[i]

    for j in range(N):
        cow = cows[j]

        unitsUp = candy_canes[i] - cane

        if cow >= unitsUp:
            dif = cow - unitsUp

            if dif > cane:
                cow += cane
                cane = 0
            else:
                cane -= dif
                cow += dif
        
        cows[j] = cow
    
    
for i in cows:
    print(i)

