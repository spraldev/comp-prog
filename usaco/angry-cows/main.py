n = 0;
arr = []

with open('angry.in', "r") as f:
    n = int(f.readline().strip())

    for i in range(n):
        arr.append(int(f.readline().strip()))

arr.sort()

print(arr)



def check_bails(i):
    
    count = 1
    j = i
    t = 1

    while j < n:
        if j == n-1:
            break


        res = []

        for k in range(j + 1, n):
            if abs(arr[j] - arr[k]) <= t:
                res.append(k)
            else:
                break
        
        if len(res) == 0:
            break

        j = res[-1]
        count += len(res)
        t += 1

    j = i
    t = 1

    while j >= 0:
        if j == 0:
            break

        res = []

        for k in range(j - 1, -1, -1):
            if abs(arr[j] - arr[k]) <= t:
                res.append(k)
            else:
                break
        
        if len(res) == 0:
            break

        j = res[-1]
        count += len(res)
        t += 1


    return count






res = 0

print(check_bails(0))

for i in range(n):
    res = max(res, check_bails(i))



with open('angry.out', "w") as f:
    f.write(str(res))
