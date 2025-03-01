
cows = []
sim = []
N = int(input())

for i in range(N):
    eek = list(map(int, input().split()))
    cows.append(eek)
    sim.append(eek.copy())




rows_final_count = 0



for i in range(N):
    odd_Sum = 0
    even_sum = 0

    for j in range(N):
        if j % 2 == 0:
            even_sum += cows[i][j]
        else:
            odd_Sum += cows[i][j]

    if even_sum > odd_Sum:
        rows_final_count += even_sum
    else:
        rows_final_count += odd_Sum

cols_final_count = 0

for i in range(N):
    odd_Sum = 0
    even_sum = 0

    for j in range(N):
        if j % 2 == 0:
            even_sum += cows[j][i]
        else:
            odd_Sum += cows[j][i]

    if even_sum > odd_Sum:
        cols_final_count += even_sum
    else:
        cols_final_count += odd_Sum



print(max(rows_final_count, cols_final_count))


# if row + 1 < len(matrix) and col + 1 < len(matrix[0]):
#             #     square = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]



#             #     maxCow = max(square)
#             #     maxIndex = square.index(maxCow)



#             #     final_count += maxCow


#             #     square.pop(maxIndex)


#             #     maxCow = max(square)
#             #     maxIndex = square.index(maxCow)

#             #     final_count += maxCow