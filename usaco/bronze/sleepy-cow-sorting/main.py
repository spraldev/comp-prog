N = 0
cows = []

with open('sleepy.in', 'r') as f:
    N = int(f.readline())
    cows = list(map(int, f.readline().split()))


i = N - 1

while i > 0 and cows[i] > cows[i - 1]:
    i -= 1


with open('sleepy.out', 'w') as f:
    f.write(str(i))
    f.write('\n')