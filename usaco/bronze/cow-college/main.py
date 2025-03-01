n = int(input())
cows = list(map(int, input().split()))

cows.sort()

money = []
charges = []

for i in range(n):
    money.append(cows[i] * (n-i))
    charges.append(cows[i])

print(max(money), charges[money.index(max(money))])