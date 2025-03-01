for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    index = nums.index(max(nums))
    cnt = 0

    while len(set(nums)  != 1):
        newIndex = 0

        if index == 0:
            newIndex = 1
        elif index == n - 1:
            
            newIndex = n - 2

        newIndex = nums.index(max(nums[index - 1], nums[index + 1]))

        nums[index] -= 1
        nums[newIndex] -= 1

        cnt += 1
        index = nums.index(max(nums))


