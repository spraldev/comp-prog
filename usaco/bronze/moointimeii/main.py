from collections import Counter as counter

N = int(input())
A = list(map(int, input().split()))

sets = []
ste = set()

for i in A:
    ste.add(i)
    sets.append(ste.copy())

inds = {}

for i in range(len(A)):
    inds[A[i]] = inds.get(A[i], []) + [i]



anws = 0

for key, val in inds.items():
    if len(val) > 1:
        second = val[-2]

        anws += len(sets[second-1])

        if second in sets[second-1]:
            anws -= 1

    
print(anws)