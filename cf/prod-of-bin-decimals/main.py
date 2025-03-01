bin_decs = []

for i in range(2, 10**5):
    if all(digit in '01' for digit in str(i)):
        bin_decs.append(i)



# precompute all nums
nums = [0] * (10**5 + 1)
nums[1] = 1

for i in range(1, 10**5 + 1):
    if i in bin_decs:
        nums[i] = 1
    else:
        for j in bin_decs:
            if i % j == 0 and nums[i//j] == 1:
                nums[i] = 1
                break

    


for _ in range(int(input())):
    n = int(input())
    print("Yes" if nums[n] == 1 else "No") 


    