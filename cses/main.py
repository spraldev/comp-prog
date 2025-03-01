strr = ""

for i in range(1, 10**3):
    strr += str(i)

for i in range(1, 100):
    if (i) % 2 == 1:
        print(str((i+(i-13)/2+1))[i % len(str((i+(i-13)/2+1)))])

# for i in range(1, 100):
#     if (i) % 2 == 1:
#         print(strr[i % len(strr)=======])