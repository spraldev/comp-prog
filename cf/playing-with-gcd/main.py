import math

def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


print(compute_lcm(4, 2))


# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))

