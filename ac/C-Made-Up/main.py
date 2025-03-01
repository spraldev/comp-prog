N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
dict_ = {}

# for i in range(N):
#     for j in range(N):
#         if A[i] == B[C[j]-1]:
#             ans += 1

for i in range(N):
    if A[i] in dict_:
        dict_[A[i]] += 1
    else:
        dict_[A[i]] = 1

for i in range(N):
    if B[C[i]-1] in dict_:
        ans += dict_[B[C[i]-1]]



print(ans)