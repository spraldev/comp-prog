import itertools
import re


letters = ['B', 'E']
N = int(input())
msgs = list(input())

def get_m():
    count = 0
    for i in range(N):
        if msgs[i] == "F":
            count += 1

    return count

def count_overlapping_occurrences(s, sub):
    if not sub:
        return len(s) + 1  
    pattern = f"(?=({re.escape(sub)}))"
    matches = re.findall(pattern, s)
    return len(matches)


sequences = itertools.product(letters, repeat=get_m())


sequences = [''.join(seq) for seq in sequences]

res_arr = []

dicts = {}

for sequence in sequences:
    copy = msgs.copy()
    seq = list(sequence)

    for i, letter in enumerate(copy):
        if letter == "F":
            copy[i] = seq.pop(0)
    
    num = count_overlapping_occurrences(''.join(copy), 'BB') + count_overlapping_occurrences(''.join(copy), 'EE')

    if num not in dicts:
        dicts[num] = [sequence]
    else:
        dicts[num].append(sequence)

    res_arr.append(num)



set_res = list(set(res_arr))
set_res.sort()

# print()


# for key, value in dicts.items():
#     print(key)
#     for i in value:
#         lstVal = list(i.lower())
#         newCopy = msgs.copy()
#         for j in range(N):
#             if newCopy[j] == "F":
#                 newCopy[j] = lstVal.pop(0)
#         print(''.join(newCopy))
#     print()


# print()
# print()
            



print(len(set_res))
print()
for i in set_res:
    print(i)
