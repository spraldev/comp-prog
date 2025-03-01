n = int(input())
flowers = list(map(int, input().split()))

final_num = 0;



for i in range(n):
    for j in range(i, n):
        avg = 0;
        count = 0;

        arrSlice = flowers[i:j+1]
        avg = sum(arrSlice) / len(arrSlice)


        for k in range(i, j+1):
            if(flowers[k] == avg):
                final_num += 1
                break;


print(final_num)