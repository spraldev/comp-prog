cowCount = 0;
sessCount = 0;
pairs = 0;

workouts = []

with open("gymnastics.in", "r") as f:
    sessCount, cowCount = map(int, f.readline().strip().split())


    for i in range(sessCount):
        workouts.append(list(map(int, f.readline().strip().split())))



for i in range(1, cowCount+1):
    currentCow = i;


    for j in range(1, cowCount+1):
        passed = False;

        if j == currentCow:
            continue;
       
        for k in range(sessCount):      
            if workouts[k].index(j) < workouts[k].index(currentCow):
                passed = True;
                break;
        
        
        
        if not passed:
            pairs += 1;


with open("gymnastics.out", "w") as f:
    f.write(str(pairs))


