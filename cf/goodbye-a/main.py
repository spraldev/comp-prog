T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    passed = False

    for i in range(len(arr) - 1):
        pair = arr[i:i+2]

        if min(pair) / max(pair) > 0.5:
            passed = True
            break

    if passed:
        print("YES")
    else:
        print("NO")


        
