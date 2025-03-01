# N, M = map(int, input().split())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# count = 0

# for i in range(N):
#     for j in range(M):
#         Next = []

#         Next.append(A[i] * B[j - 1] if j - 1 >= 0 else 0)

#         Next.append(A[i] * B[j + 1] if j + 1 < M else 0)

#         Next.append(A[i - 1] * B[j] if i - 1 >= 0 else 0)

#         Next.append(A[i + 1] * B[j] if i + 1 < N else 0)

#         if max(Next) < A[i] * B[j]:
#             count += 1

# print(count)