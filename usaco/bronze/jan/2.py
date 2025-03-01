from collections import Counter

N = int(input())
nums = list(map(int, input().split()))

freq = Counter(nums)

numsset = {}
for item in nums:
    numsset[item] = None

set_nums = list(numsset.keys())

cont = 0

#56344
already = set()

for (i, v) in enumerate((set_nums)):
    if freq[v] >= 2 and v not in already:
        cont += i
        already.add(v)

print(cont)
