T = int(input())

final_result = []

def is_majority(lst, element):
    return lst.count(element) > len(lst) / 2

def solve(N, A):
    arr = []

    for i in range(N):
        for j in range(i+1, N):
            sub = A[i:j+1]

            for k in range(len(set(sub))):
                if is_majority(sub, list(set(sub))[k]) and list(set(sub))[k] not in arr:
                    arr.append(list(set(sub))[k])

    if len(arr) > 0:
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