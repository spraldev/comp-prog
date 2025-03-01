N, Q = map(int, input().split())
A = list(map(int, input().split()))
sumA = []
sumNum = 0

for i in A:
    sumNum += i
    sumA.append(sumNum)

for _ in range(Q):
    nums = list(map(int, input().split()))
    l = nums[0] - 1
    r = nums[1] -1

    anws = 0

    if l + 1 == r:
        anws = A[l + 1]
    elif l == -1:
        anws = sumA[r]
    else:
        anws = sumA[r] - sumA[l]

    print(anws)