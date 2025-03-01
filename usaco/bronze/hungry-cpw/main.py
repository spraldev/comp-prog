N, T = map(int, input().split())
lastDay = 0
bales = 0
anws = 0
lastAnws = 0


for _ in range(N):
    delivery = list(map(int, input().split()))
    if delivery[0] > T:
        # get the days inbetween the last day and T
        x = min(T - lastDay, bales)
        bales += x
        break


    x = min(delivery[0] - lastDay- 1, bales)
    bales -= x
    bales += delivery[1] -  1
    
    
    anws += x + 1
    # print("day", delivery[0])
    # print("bales", bales)
    # print("difference in days", delivery[0] - lastDay)
    # print("anwsdiff", anws - lastAnws)

    # print()
    # print()



    lastDay = delivery[0]
    lastAnws = anws


if lastDay < T:
    x = min(T - lastDay, bales)
    bales -= x
    anws += x

print(anws)
