
#################################################################################
# SCRATCH PAPER WORK LOLOLOL
#################################################################################

# from tqdm import tqdm
# nums = set()

# for n in tqdm(range(1, 100000001)):
#     x = sum([int(x) for x in list(str(n))])
#     y = sum([int(x) for x in list(str(n+1))])

#     if not (y-x == 1 or (abs(y-x) % 9 == 8 and abs(y-x) >=9 and (y-x) < 0) or (y-x == -8)):
#         print("ERROR FOUND")
#         print("N: " + str(n))
#         print("x: " + str(sum([int(x) for x in list(str(n))])))
#         print("y: " + str(sum([int(x) for x in list(str(n+1))])))
#         # break


#     nums.add(sum([int(x) for x in list(str(n+1))]) - sum([int(x) for x in list(str(n))]))

#     # print()
#     # print()

# print(sorted(list(nums), reverse=True))


for _ in range(int(input())):
    x, y = map(int, input().split())

    print("YES" if (y-x == 1 or (abs(y-x) % 9 == 8 and abs(y-x) >=9 and (y-x) < 0) or (y-x == -8)) else "NO")