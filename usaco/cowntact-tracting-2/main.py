N = int(input())
A = list(map(int, list(input())))

count = 0
arr = []


for i in range(len(A)):
    if A[i] == 1:
        count += 1
    else:
        if count > 0:
            arr.append(count)
        count = 0

if count > 0:
    arr.append(count)


anws = 0

for i in arr:
    if i/N >= 0.3:
        anws += 1
    else:
        anws += 2


def check_zeroth_day(newA):

    for i in range(len(newA)):

        if i == len(newA) - 1:
            if newA[i] == 1 and newA[i-1] == 0:
                return True
            else:
                return False
        elif i == 0:
            if newA[i] == 1 and newA[i+1] == 0:
                return True
        else:
            if newA[i] == 1 and newA[i-1] == 0 and newA[i+1] == 0:
                return False
            

    return False

        

        


print(A.count(1) if check_zeroth_day(A) else anws)

#print(anws)