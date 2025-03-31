N, A, B = map(int, input().split())

cows = []
hashmap = {}

for _ in range(N):
    cows.append(list(map(int, input().split())))
    hashmap[cows[-1][1]] = cows[-1][0]

anws = 0

for cow_id, num_cows in hashmap.items():
    target_1 = A - cow_id
    target_2 = B - cow_id

    anws_add = 0
    other_cow = -1
    sub_amount = 0


    if cow_id * 2 == B or cow_id * 2 == A:
        pot = num_cows // 2

        if pot > anws_add:
            anws_add = pot
            other_cow = cow_id
            sub_amount = hashmap[cow_id]



    if target_1 in hashmap and target_1 != cow_id:
        pot = min(num_cows, hashmap[target_1])

        if pot > anws_add:
            anws_add = pot
            other_cow = target_1
            sub_amount = hashmap[target_1]

    if target_2 in hashmap and target_2 != cow_id:
        pot = min(num_cows, hashmap[target_2])

        if pot > anws_add:
            anws_add = pot
            other_cow = target_2
            sub_amount = hashmap[target_2]



    if other_cow != -1:
        if hashmap[other_cow] ==hashmap[cow_id]:
            hashmap[other_cow] -= anws_add
        else:
            hashmap[other_cow] -= anws_add
            hashmap[cow_id] -= anws_add
            
        anws += anws_add


print(anws)



