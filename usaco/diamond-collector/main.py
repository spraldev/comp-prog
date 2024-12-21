n = 0;
k = 0;
diamonds = []

with open("diamond.in", "r") as fin:
    n, k = map(int, fin.readline().strip().split())

    for i in range(n):
        diamonds.append(int(fin.readline().strip().split()[0]))


print(diamonds)

i = 0;

arrr = []

print("\n\n")

for _ in range(n):
    arr = []

    count = 0;

    print(diamonds[i])
    print("\n\n")

    for diamond in diamonds:
        if(i == n-1):
            break
        if(i== diamonds.index(diamond)):
            continue;
        
        print(diamonds[i], diamond)
        print(abs(diamonds[i] - diamond))


        if abs(diamonds[i] - diamond) <= k:
            arr.append(diamond)
            print('adding')
            print(arr)

        print("--------")

    print("\n\n")

    arrr.append(len(arr))

    i += 1;




print(arrr)

with open("diamond.out", "w") as fout:
    fout.write(str(max(arrr)))


    



