#BONOUS: 7 liner solution lol
# from collections import Counter
# N, A = int(input()), list(map(int, input().split()))
# c = Counter(A)
# m = 0
# for i in range(N+1):
#     print(max(m, c[i]))
#     m += c[i] == 0

N = int(input())
a = list(map(int, input().split()))

def frequency_dictionary(my_list):
    frequency = {}
    for item in my_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

freq = frequency_dictionary(a)

# current Mex

def mex(my_list):
    for i in range(len(my_list)):
        if i not in my_list:
            return i
    return len(my_list)

current_mex = mex(a)

missing_arr = []

for i in range(N+1):
    if i == 0:
        missing_arr.append(0)
        continue
    missing_arr.append(missing_arr[i-1] + (1 if i-1 not in freq else 0))
    
    
for i in range(N+1):
    if i == current_mex:
        print(0)
        continue

    # to make i the mex, the array must contain all numbers from 0 to i-1

    # vals = range(i)

    count_i = freq.get(i, 0)
    # how many vals are missing from the array
    missing = missing_arr[i]

    print(max(missing, count_i))
