N, K = 0,0
arr = []

with open("diamond.in", "r") as f:
    N, K = map(int, f.readline().split())
    for i in range(N):
        arr.append(int(f.readline()))

anws = 0

for i in range(N):
    diamond = arr[i]

    new_arr = []
    counter = 0

    for diamond2 in arr:
         if diamond <= diamond2 <= diamond + K:
            new_arr.append(diamond2)
            counter += 1

            if diamond2 == 6:
                print(diamond - diamond2)

    print(new_arr, diamond)

    anws = max(anws, counter)





    


with open("diamond.out", "w") as f:
    f.write(str(anws))

