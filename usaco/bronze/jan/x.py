N = int(input())
nums = list(map(int, input().split()))

moos = set()

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if nums[i] != nums[j] and nums[j] == nums[k]:
                moos.add(str(nums[i])  + str(nums[j]) + str(nums[k]))



print(len(moos))