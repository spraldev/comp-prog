N = int(input())
bacteria = list(map(int, input().split()))

offset = 0
mult_sum = 0
count = 0

for i in range(N):
    bacteria[i] += offset

    mul = bacteria[i] * -1

    if i == N-1:
        bacteria[i] += mul
        count += abs(mul)
        break
    
    mult_sum += mul

    offset += mult_sum + mul
    bacteria[i] += mul

    count += abs(mul)

print(count)
