import sys

# sys.stdin = open("cowcode.in", "r")
# sys.stdout = open("cowcode.out", "w")

# imp = input().split()
# s = imp[0]
# n = int(imp[1])

s = input()


def rot(s) -> str:
    return s[-1] + s[:-1]

new_s = s

for i in range(3):
    new_s += rot(new_s)

print(new_s)

# print()
# print()
# for i in range(len(new_s)):
#     print(new_s[i], end=" ")

# print()

# for i in range(len(new_s)):
#     print(i+1, end=" ")


for i in range(len(new_s)):
    print(s.index(new_s[i]))