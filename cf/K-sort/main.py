for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    out_of_place = []

    if len(A) == 1:
        print(0)
        continue

    for i in range(N):
        if i == 0:
            if not(A[i] <= A[i+1]):
                # calculate the minimum number of additions needed to make A[i] in place
                out_of_place.append((i, A[i], A[i] - A[i+1]))
        elif i == N - 1:
            if not(A[i-1] <= A[i]):
                out_of_place.append((i, A[i], A[i] - A[i-1]))
        else:
            if not(A[i-1] <= A[i] <= A[i+1]):
                # calculate the minimum number of additions needed to make A[i] in place (so greater than A[i-1] and less than A[i+1])
                out_of_place.append((i, A[i], max(A[i-1], A[i+1]) - A[i]))

    if len(out_of_place) == 0:
        print(0)
        continue

    anws = 0

    out_of_place = [out_of_place[i] if out_of_place[i][2] > 0 else None for i in range(len(out_of_place))]

    for i in range(len(out_of_place)):
        