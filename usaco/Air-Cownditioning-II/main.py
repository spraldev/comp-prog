from itertools import chain, combinations

def all_subsets(array):
    return list(chain.from_iterable(combinations(array, r) for r in range(len(array) + 1)))


n, m = map(int, input().split())

sim = [0] * 100

cows = []
acs = []
final_prices = []

for i in range(n):
    cows.append(list(map(int, input().split())))

for i in range(m):
    acs.append(list(map(int, input().split())))


for i in range(len(cows)):
    for j in range(cows[i][0] - 1, cows[i][1]):
        sim[j] = cows[i][2]


for subset in all_subsets(acs):
    successful = False
    money = 0
    copy = sim.copy()

    
    for i in range(len(subset)):
        #print(subset[i])
        money += subset[i][3]
        for j in range(subset[i][0] - 1, subset[i][1]):
            copy[j] -= subset[i][2]
            
    
    for i in range(len(copy)):
        if copy[i] > 0:
            successful = False
            break
        else:
            successful = True
    
    #print(successful)
    #print(money)
    #print(copy)
    
    #print("\n\n")


    if successful:
        final_prices.append(money)


print(min(final_prices))