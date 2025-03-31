import itertools
import math



def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# def gen_valid_perms(n):

#     perms = itertools.permutations(range(1, n + 1))
#     valid_perms = []
#     invalid_perms = []


    

#     for perm in perms:
#         C = []
#         cum = list(itertools.accumulate(perm))

#         for i in range(n):
#             C.append(math.ceil(cum[i]/(i + 1)))

#         prine_goal = math.floor(n/3) - 1

#         for i in C:
#             if is_prime(i):
#                 prine_goal -= 1

#         if prine_goal <= 0:
#             valid_perms.append(perm)
            
#         else:
#             invalid_perms.append(perm)
#             print(perm)

#     return valid_perms


def check_if_valid(perm, n):
    C = []
    cum = list(itertools.accumulate(perm))

    for i in range(n):
        C.append(math.ceil(cum[i]/(i + 1)))

    prine_goal = math.floor(n/3) - 1

    for i in C:
        if is_prime(i):
            prine_goal -= 1

    if prine_goal <= 0:
        return True
    else:
        return False

