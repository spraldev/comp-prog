from itertools import combinations

arr = list(map(int, input().split()))
largest = arr.pop(arr.index(max(arr)))


subsets = list(combinations(arr, 3))

for subset in subsets:
    if sum(subset) == largest:
        sorted_subset = sorted(subset)
        print(' '.join(map(str, sorted_subset)))
        break
