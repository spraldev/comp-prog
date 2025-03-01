import sys

sys.stdin = open("highcard.in")
sys.stdout = open("highcard.out", "w+")

n = int(input())
elsie_has = set()
for i in range(n):
	elsie_has.add(int(input()))


elsie, bessie = [], []

for i in range(1, n * 2 + 1):

	if i not in elsie_has:
		bessie.append(i)
	else:
		elsie.append(i)


bessie.sort()
elsie.sort()

points = 0
for i in range(n):
    if bessie[i] < elsie[i]:
        points += 1


print(points)