n = int(input())
flowers = list(map(int, input().split()))

final_num = n




for i in range(n):
    for j in range(n):
        if(j < 2):
            continue;
        
        avg = 0;
        count = 0;

        if(i+j > n):
            break;
        
        print(i+j+1)

        for k in range(i, i+j+1):
            avg += flowers[k]
            count += 1


        avg = avg / count


        for k in range(i, i+j):
            if(k+1 > n):
                break;
            

            if(flowers[k] == avg):
                final_num += 1
                break;

        
        

print(final_num)