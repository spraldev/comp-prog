N = 0
logs = []

with open("taming.in", "r") as f:
    N = int(f.readline().strip())
    logs = list(map(int, f.readline().strip().split()))

logs[0] = 0



for i in range(len(logs) - 2):
    chunk = logs[i:i+3]

    if chunk[0] == -1 or chunk[1] != -1 or chunk[2] == -1 or len(chunk) != 3:
        continue

    if chunk[2] - chunk[0] != 2 and chunk[2] != 1 and chunk[0] != 0 and chunk[2] != 0:
        with open("taming.out", "w") as f:
            f.write("-1")
        exit()

if logs[1] > 1:
    with open("taming.out", "w") as f:
        f.write("-1")
    exit()




firstOcurr = logs.index(-1)

i = firstOcurr-1

k = firstOcurr

while logs[k] == -1:
    if k == N-1:
        break

    k += 1



while True:
    if k == N-1 and logs[k] == -1:
        for j in range(i+1, k + 1):
            if logs[j] == -1:
                logs[j] = -2
            else:
                logs[j] = 0
        break


    if logs[k - logs[k]] == -1:
        logs[k - logs[k]] = 0

        for j in range(i+1, k - logs[k] + 1):
            if logs[j] == -1:
                logs[j] = -2

    elif logs[k] == 0:
        for j in range(i+1, k+1):
            if logs[j] == -1:
                logs[j] = -2

    try:
        firstOcurr = logs.index(-1, k)
    except:
        break
    i = firstOcurr-1

    k = firstOcurr

    while logs[k] == -1:
        if k == N-1:
            break

        k += 1

    if k == N-1:
        break

with open("taming.out", "w") as f:
    f.write(str(logs.count(0)) + " " + str(logs.count(0) + logs.count(-2)))