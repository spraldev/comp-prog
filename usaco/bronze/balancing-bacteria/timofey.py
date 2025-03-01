N = int(input())
bac = list(map(int, input().split()))

ans = 0

for i in range(N):
	if i == 0:
		continue;
	
	ans += abs(bac[i]) - abs(bac[i-1])

print(ans)
