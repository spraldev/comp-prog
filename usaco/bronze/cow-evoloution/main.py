N = 0
arr = []

with open('evolution.in', 'r') as f:
    N = int(f.readline())
    
    for _ in range(N):
        line = f.readline().strip().split()
        arr.append((int(line[0]), line[:1]))


for i in range(N):
    group = arr[i]
    for j in range(arr[i][0]):
        for k in range(N):
            if i == k:
                continue

            simPass = True

            for l in range(min(len(group[1]), len(arr[k][1]))):
                #if the group is not a subset of the other group
                if group[1][l] != arr[k][1][l]:
                    simPass = False
                    break

            if set(group[1]) & set(arr[k][1]) and not simPass:
                with open('evoloution.out', 'w') as f:
                    f.write('no')
                exit(0)

with open('evolution.out', 'w') as f:
    f.write('yes')