N = int(input())
cows = list(input())

count = 0

#GGG


# for i in range(N):
#     gCount = 0
#     hCount = 0

#     for j in range(i, N):
#         if cows[j] == 'G':
#             gCount += 1
#         else:
#             hCount += 1


#         if gCount + hCount >= 3:
#             if gCount == 1:
#                 count += 1

#             if hCount == 1:
#                 count += 1


recentG = -1
recentH = -1
secondRecentG = -1
secondRecentH = -1

#GHG

count = 0


for i in range(N):
    if cows[i] == 'G':
        secondRecentG = recentG
        recentG = i
    else:
        secondRecentH = recentH
        recentH = i

    if i < 2:
        continue

    if recentG >= i-2 and recentH >= i-2:
        count += (i - 2) - min(secondRecentG, secondRecentH)
    elif recentG >=0 and recentH >= 0:
        count += min(recentG, recentH) - min(secondRecentG, secondRecentH)
        






print(count)