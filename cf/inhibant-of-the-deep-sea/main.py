for _ in range(int(input())):
    N, K, = map(int, input().split())
    arr = list(map(int, input().split()))
    leftAttacks = 0
    rightAttacks = 0

    if K % 2 == 0:
        leftAttacks = K // 2
        rightAttacks = K // 2
    else:
        leftAttacks = K // 2 + 1
        rightAttacks = K // 2

    cnt = 0


    i = 0
    while i < len(arr):
        if arr[i] <= leftAttacks and leftAttacks > 0:
            cnt += 1
            leftAttacks -= arr[i]
            arr.pop(i)
        else:
            break

    if len(arr) == 0:
        print(cnt)
        continue
    elif len(arr) == 1:
        if arr[0] <= rightAttacks:
            cnt += 1
        print(cnt)
        continue


    for i in range(len(arr)-1, -1, -1):
        if arr[i] <= rightAttacks and rightAttacks > 0 :
            cnt += 1
            rightAttacks -= arr[i]
        else:
            break

    print(cnt)


