for _ in range(int(input())):
    n = int(input())
    
    nums = [15, 10, 6, 3, 1]

    res = 0
    if n in nums:
        print(1)
        continue

    e = 1

    for num in nums:
        if n >= num:
            res += n // num
            n %= num
            
    print(res, n, e)
    

    