N = int(input())
ideal = list(map(int, input().split()))
current = list(map(int, input().split()))

count = 0

diffs = [ideal[i] - current[i] for i in range(N)]
 
op = 0

for i in range(len(diffs)):
    
    keep = op - abs(diffs[i])
    # print(count, op, keep)
    if keep < 0:
        count += abs(keep)
    
    op = abs(diffs[i])


    if i != len(diffs) - 1 and diffs[i+1] * diffs[i] < 0:
        op = 0

    

print(count)
