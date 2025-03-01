for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))



    count  = 0
    sumA = A[0]

    for i in range(1, N):
        
        
        print(sumA, A[:i], sumA in A[:i])
    
        if sumA in A[:i+1]:
            count += 1

        sumA += A[i]

        



    print(count)