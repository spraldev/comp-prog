from itertools import combinations

n = int(input())
a = list(map(int, input().split()))

a.sort()

people = n * 2
kyaks = n - 1

res = 0

totInstability = 0


# a.pop(len(a) - 1)
# a.pop(len(a) - 1)

def disjoint_pairs(arr):
    if len(arr) == 2:
        return [[(arr[0], arr[1])]]  
    pairs = []
    for pair in combinations(arr, 2):
        remaining = [x for x in arr if x not in pair]
        for rest in disjoint_pairs(remaining):
            pairs.append([pair] + rest)

    return pairs


while(len(a) > 2):
    diffs = []
    disjointPairs = disjoint_pairs(a)
    flattened_disjointPairs = [tuple(pair) for partition in disjointPairs for pair in partition]


    for i, pair in enumerate(flattened_disjointPairs):
        diffs.append(abs(pair[0] - pair[1]))

    totInstability += min(diffs)
    a.remove(max(flattened_disjointPairs[diffs.index(min(diffs))]))
    a.remove(min(flattened_disjointPairs[diffs.index(min(diffs))]))




print(totInstability)