for _ in range(int(input())):
    N, doses, dose_life, max_wait = map(int, input().split())
    T = list(map(int, input().split()))

    cnt = 1
    current_pack = 0
    start = T[0]

    for i in range(N):
        if current_pack >= doses:
            cnt += 1
            current_pack = 1
            start = T[i]
            continue

        if start  + max_wait + dose_life < T[i]:
            cnt += 1
            current_pack = 1
            start = T[i]
            continue

        if T[i] - (start + max_wait) > dose_life:
            cnt += 1
            current_pack = 1
            start = T[i]
            continue


        current_pack += 1


    print(cnt)
