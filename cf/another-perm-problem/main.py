import itertools
from tqdm import tqdm

lst = [0, 0, 0]

def get_perms(n):
    perms = list(itertools.permutations(range(1, n+1)))
    return perms

def get_max_cost(perms):
    ret = 0

    for perm in perms:
        sum1 = 0
        sum2 = 0    
        
        for i in range(len(perm)):
            sum1 += perm[i] * (i+1)
        
        for i in range(len(perm)):
            sum2 = max(sum2, perm[i] * (i+1))

        final_num = sum1 - sum2

        ret = max(ret, final_num)

    return ret


for i in tqdm(range(2, 250), desc="Processing"):
    perms = get_perms(i)
    lst.append(get_max_cost(perms))

print(lst)
