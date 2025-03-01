import sys
from itertools import accumulate

sys.stdin = open('highcard.in', 'r')
sys.stdout = open('highcard.out', 'w')

elsie_has = set()
N = int(input())

for i in range(N):
	elsie_has.add(int(input()))

elsie, bessie = [], []

for i in range(1, N * 2 + 1):
	if i not in elsie_has:
		bessie.append(i)
	else:
		elsie.append(i)

bessie.sort()
bessie_index, elsie_index, score = 0, 0, 0
elsie.sort()


while bessie_index < N and elsie_index < N:
    if bessie[bessie_index] > elsie[elsie_index]:
        score += 1
        elsie_index += 1
        bessie_index += 1
    else:
        bessie_index += 1

print(score)