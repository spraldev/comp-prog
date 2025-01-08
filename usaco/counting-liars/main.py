import itertools


less_than = []
greater_than = []


N = int(input())
for i in range(N):
    x = input().split()

    if x[0] == 'G':
        greater_than.append(int(x[1]))
    else:
        less_than.append(int(x[1]))

cows = []
other = []
anws = 0
for i in range(len(greater_than)):
    for j in range(len(less_than)):
        cows.append((greater_than[i]))
        other.append((less_than[j]))

        if 

        if greater_than[i] > less_than[j]:
            anws += 1


print(anws)