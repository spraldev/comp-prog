import itertools


less_than = []
greater_than = []

pos = []


N = int(input())
for i in range(N):
    x = input().split()

    if x[0] == 'G':
        greater_than.append(int(x[1]))
    else:
        less_than.append(int(x[1]))

    pos.append(x[1])
    


anws = float('inf')

for poss in pos:
    cont = 0

    for i in less_than:
        if int(poss) > int(i):
            cont += 1

    for i in greater_than:
        if int(poss) <q int(i):
            cont += 1

    anws = min(anws, cont)



print(anws)