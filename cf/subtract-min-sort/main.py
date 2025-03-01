for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))


    passed = False

    for i in range(N):
        if i == N-1:
            continue

        if i > 0 and A[i] < A[i+1]:
            passed = True
            break

    print("YES" if passed else "NO")