import sys

# sys.stdin = open('homework.in', 'r')
# sys.stdout = open('homework.out', 'w')

N = int(input())
A = list(map(int, input().split()))

dictr = {}

aSum = sum(A)
sortedA = sorted(A)
minDict = {}

def values_to_positions(lst):
    unique_vals = set(lst)
    
    sorted_vals = sorted(unique_vals) 
    
    val_to_pos = {val: idx for idx, val in enumerate(sorted_vals)} 

    return val_to_pos



minDict = values_to_positions(A)
minVal  = min(A)



for i in range(N):
    arr = A[i+1:]

    if len(arr) == 0 or len(arr) == 1 or len(arr) == 2:
        continue

    aSum -= A[i]
    minDict.pop(A[i])
    minVal = min(minDict.keys())
    newSum = aSum - minVal
    avg = newSum / len(arr)
    dictr[i+1] = avg
    



# get all keys with max value
scores = [k for k, v in dictr.items() if v == max(dictr.values())]
print(*scores)