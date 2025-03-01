T = int(input())

final_result = []

def is_majority(lst, element):
    return lst.count(element) > len(lst) / 2

def solve(N, A):
    arr = []

    if len(A) == 2:
        if A[0] == A[1]:
            final_result.append(str(A[0]))
        else:
            final_result.append(-1)
        return

    for i in range(N - 2):
        three = A[i:i+3]

        if three[0] == three[1] or three[0] == three[2] and three[0] not in arr:
            arr.append(three[0])
        elif three[1] == three[2] or three[1] == three[0] and three[1] not in arr:
            arr.append(three[1])
        elif three[2] == three[0] or three[2] == three[1] and three[2] not in arr:
            arr.append(three[2])

    if len(arr) > 0:
        arr = list(set(arr))
        arr.sort()
        final_result.append(" ".join(map(str, arr)))
    else:
        final_result.append(-1)



for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)

for result in final_result:
    print(result)