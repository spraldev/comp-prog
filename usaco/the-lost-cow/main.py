x = 0
y = 0

with open("lostcow.in", "r") as f:
    content = f.read()

    x = int(content.split()[0])
    y = int(content.split()[1])



newnum = x;
newnumReverse = x;


reverse = False;
difference = 1;

done = False
miles = 0


print(x, y)


while done == False:
    if(reverse):
        newnumReverse = newnumReverse  - difference

        if(newnumReverse  <= y and y <= x):
            done = True
            miles = miles + difference
            break
        else:
            miles += difference * 2



        reverse = not reverse


    else:
        newnum = newnum + difference

        miles += difference * 2
        
        

        if(newnum >= y and y >= x):
            done = True
            miles = miles + difference
            break
        else:
            miles += difference * 2

        reverse = not reverse

   


print(miles)