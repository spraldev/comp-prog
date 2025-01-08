n = 0;
arr = []

with open('angry.in', "r") as f:
    n = int(f.readline().strip())

    for i in range(n):
        arr.append(int(f.readline().strip()))

arr.sort()

print(arr)



def check_bails(i):

    counter = 1

    # for j in range(i, n):

    #     if j == n-1:
    #         continue

    #     blastRadius = j-i
        
    #     if abs(arr[j] - arr[j+1]) <= blastRadius:
    #         counter += 1
    #     else:
    
    #         counter += 1
    #         break

    j = 0

    while j < n:
        if j == n-1:
            break

        if abs(arr[j] - arr[j+1]) <= i:
            counter += 1
            j += 1
        else:
            break

    

    # for j in range(i, -1, -1):

    #     if j == 0:
    #         continue

    #     blastRadius = i-j+1

    #     if abs(arr[j] - arr[j-1]) <= blastRadius:
    #         counter += 1
    #     else:
    #         break

    j = n-1

    while j > 0:

        if j == 0:
            break
        
        if abs(arr[j] - arr[j-1]) <= i:
            counter += 1
            j -= 1
        else:
            break

    return counter





res = 0

print(check_bails(0))

for i in range(n):
    res = max(res, check_bails(i))



with open('angry.out', "w") as f:
    f.write(str(res))
