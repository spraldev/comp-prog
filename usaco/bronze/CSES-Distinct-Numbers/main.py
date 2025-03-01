from array import array


n = int(input())
arr = list(map(int, input().split()))


newArr = array("i", arr)

sortedarr = sorted(arr)

distinct = 0

for i in range(n):
    if(sortedarr[i] != sortedarr[i-1]):
        distinct += 1

if(distinct == 0):
    distinct = 1

print(distinct)

