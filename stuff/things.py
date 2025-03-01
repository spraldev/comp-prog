

for _ in range(int(input())):
    n = int(input())
    arr = list(input())
    arr = [int(x) - 1 for x in arr]
    
    prefsun = [0]

    for i in arr:
        prefsun.append(prefsun[-1] + i)

    
    
    prefsun.pop(0)



    hashmap = {0: 1}

    cont = 0


    for i in prefsun:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

            cont += hashmap[i] - 1

    print(cont)