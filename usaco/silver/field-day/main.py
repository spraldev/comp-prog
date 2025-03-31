import itertools

C, N = map(int, input().split())
teams = [0] * N


for i in range(N):
	breeds = input()

	for j in range(C):
		if breeds[j] == "G":
			teams[i] += 1 << (C - j - 1)
			
ste = set(teams)
nonNumLst = list(itertools.product([0, 1], repeat=C))
lst = []


for i in range(len(nonNumLst)):
	lst.append(int(''.join(map(str, nonNumLst[i])), 2))

for team in teams:
	dif = 0

	for i in lst:
		if i != team and i in ste:
			dif = max(dif, bin(team ^ i).count("1"))
			
	print(dif)