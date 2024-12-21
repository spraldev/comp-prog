n, m, k = 0, 0, 0
order = []
places = []


with open("milkorder.in", "r") as f:
    n, m, k = map(int, f.readline().strip().split())
    order = [int(x) for x in f.readline().strip().split()]

    
    for i in range(k):
        line = f.readline().strip().split()
        places.append((int(line[0]), int(line[1])))


arr = [0] * n

for i in range(len(places)):
    arr[places[i][1]-1] = places[i][0]


filtered_order = [item for item in order if item not in arr and item != 1]
check_order = order.copy()
order = filtered_order


anwsers = []

copy = arr.copy()
orderCopy = order.copy()

print("arr", arr)
print("order", order)
print("places", places)

print("\n\n")

for i in range(len(arr)):
    if arr[i] != 0:
        continue;

    arr[i] = 1


    if len(order) != 0:
        for j in range(len(arr)):
            if arr[j] == 0:
                arr[j] = order[0]
                order.remove(order[0])
                
                
                if len(order) == 0:
                    break

    
    if 2 == 2:
        print("checking position", i + 1, "arr", arr)
        print("order", check_order)

    indices_map = {value: idx for idx, value in enumerate(arr)}

    if 2 == 2:
        print("indices map", indices_map)

    orderCorrect = True

    for j in range(1, len(check_order)): 
        prev_index = indices_map.get(check_order[j-1], -1)
        curr_index = indices_map.get(check_order[j], -1)

        if 2 == 2:

            print(check_order[j-1])

        if prev_index > curr_index:
            if 2 == 2:
                print(f"Order incorrect at index {j}: {check_order[j-1]} ({prev_index}) > {check_order[j]} ({curr_index})")
            orderCorrect = False
            break 



    if orderCorrect:
        anwsers.append(i+1)
        print("order correct", i+1, arr)

    arr = copy.copy()
    order = orderCopy.copy()



print(anwsers)

with open("milkorder.out", "w") as f:
    f.write(str(min(anwsers)))
        
        




################################################################
# OLD CODE
################################################################

        # for j in range(len(arr)):
        #     if arr[j] == 0:
        #         arr[j] = order[0]
        #         order.remove(order[0])
                
                
        #         if len(order) == 0:
        #             break

        # indexes = []

        # for j in range(len(order)):
        #     if order[j] in arr:
        #         indexes.append(j)
            
        # for j in range(len(indexes)):
        #     cowIndex = arr.index(order[indexes[j]])
        #     otherIndex = 0
            
        #     if j == 0:
        #         otherIndex = 0
        #     else:
        #         otherIndex = arr.index(order[indexes[j-1]])

        #     # insert every cow from order[indexes[j-1]] to order[indexes[j]] into the array
        #     for k in range(otherIndex, cowIndex):
        #         if arr[k] == 0:
        #             continue
        #         else:
        #             arr[k] = order[indexes[j]]
        #             order.remove(order[indexes[j]])
        #             if len(order) == 0:
        #                 break