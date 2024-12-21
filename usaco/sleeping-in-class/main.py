T = int(input())

ans = []

for i in range(T):
    n = int(input())
    a = list(map(int, input().split()))

    Sum = sum(a)

    test_anws = []

    for j in range(Sum + 1):
        if j != 0 and Sum % j != 0 or j == 0:
            continue;

        

        target = Sum / j

        passed = True


        for k in range(n):
            if a[k] > target:
                passed = False
                break

            if a[k] == -1 or k == n-1:
                continue
            
            a[]




        if passed:


        

        

        

        

    


    