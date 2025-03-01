values = [0] * 60
nums = [1, 3, 6, 10, 15]

for i in range(60):
    for num1 in nums:
        if num1 == i:
            values[i] = 1
            break
        for num2 in nums:
            if num1 + num2 == i:
                values[i] = 2
                break
            for num3 in nums:
                if num1 + num2 + num3 == i:
                    values[i] = 3
                    break
                for num4 in nums:
                    if num1 + num2 + num3 + num4 == i:
                        values[i] = 4
                        break
                    for num5 in nums:
                        if num1 + num2 + num3 + num4 + num5 == i:
                            values[i] = 5
                            break



print(values) 




for _ in range(int(input())):
    n = int(input())
    count = 0


    while n > 60:
        n -= 15
        count += 1

    pr

