for _ in range(int(input())):
    s = input()
    arr = [int(x) for x in s]
    n = 0

    for i in range(len(arr) - 1, -1, -1):
        if i == 0 or arr[i] == 0:
            continue

        new_S = arr.copy()


        num = new_S.pop(i)
        new_S.insert(i - 1, num - 1)

        if int("".join([str(x) for x in new_S])) > n:
            n = int("".join([str(x) for x in new_S]))
            arr = new_S

    print(n)