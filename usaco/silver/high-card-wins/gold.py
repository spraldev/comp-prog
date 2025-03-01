import sys

sys.stdin = open('cardgame.in', 'r')
sys.stdout = open('cardgame.out', 'w')

elsie_has = set()
N = int(input())

half = N//2

for i in range(N):
	elsie_has.add(int(input()))

elsie, bessie = [], []

for i in range(1, N * 2 + 1):
	if i not in elsie_has:
		bessie.append(i)
	else:
		elsie.append(i)

bessie.sort()
elsie.sort()

bessie_first = bessie[half:]
bessie_second = bessie[:half]

elsie_first = elsie[half:]
elsie_second = elsie[:half]

bessie_index, elsie_index, score = 0, 0, 0


while bessie_index < half and elsie_index < half:
    if bessie_first[bessie_index] > elsie_first[elsie_index]:
        score += 1
        elsie_index += 1
        bessie_index += 1
    else:
        bessie_index += 1
		
bessie_index, elsie_index = 0, 0
bessie_second.sort(reverse=True)
elsie_second.sort(reverse=True)

while bessie_index < half and elsie_index < half:
    if bessie_second[bessie_index] < elsie_second[elsie_index]:
        score += 1
        elsie_index += 1
        bessie_index += 1
    else:
        bessie_index += 1

print(score)