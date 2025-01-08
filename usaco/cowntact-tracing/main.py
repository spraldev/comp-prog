N, T = list(map(int, input().split()))
cows = list(map(int, list(input())))

records = [0] * T

for i in range(T):
    rec = list(map(int, input().split()))
    rec[1] -= 1
    rec[2] -= 1

    records[i] = rec

records.sort(key=lambda x: x[0])


inf_cows = []

for i in range(T):

    print(records[i][1])

    if cows[records[i][1]] == 1 and cows[records[i][2]] == 1:
        if records[i][1] not in inf_cows:
            inf_cows.append(records[i][1])
            


print(inf_cows)
