import itertools
import re


# letters = ['B', 'E']
N = int(input())
msgs = list(input())


arr = []
dicts = {'FFF': [0, 1, 2], 'FFE': [0, 1, 2], 'FFB': [0, 1, 2], 'FEF': [0, 1, 2], 'FEE': [1, 2], 'FEB': [0, 1], 'FBF': [0, 1, 2], 'FBE': [0, 1], 'FBB': [1, 2], 'EFF': [0, 1, 2], 'EFE': [0, 2], 'EFB': [1], 'EEF': [1, 2], 'EEE': [2], 'EEB': [1], 'EBF': [0, 1], 'EBE': [0], 'EBB': [1], 'BFF': [0, 1, 2], 'BFE': [1], 'BFB': [0, 2], 'BEF': [0, 1], 'BEE': [1], 'BEB': [0], 'BBF': [1, 2], 'BBE': [1], 'BBB': [2]}


for i in range(0, len(msgs), 3):
    chunk = "".join(msgs[i:i+3])

    if len(arr) == 0:
        arr = dicts[chunk].copy()
        continue
    
    match chunk:
        case "FFF":
            new_arr = []
            for i in range(arr[0], arr[-1] + 1):
                new_arr.append(i)

            # append the 3 next numbers after new_arr[-1]. 
            for i in range(1, 4):
                new_arr.append(arr[-1] + i)
            
            arr = new_arr.copy()
        case "BFF":
            new_arr = []
            for i in range(arr[0], arr[-1] + 1):
                new_arr.append(i)

            # append the 2 next numbers after new_arr[-1]. 
            
            for i in range(1, 3):
                new_arr.append(arr[-1] + i)

            arr = new_arr.copy()

print(arr)
                
    






# print(len(set_res))
# print()
# for i in set_res:
#     print(i)

    


        








