for _ in range(int(input())):
    n = int(input())
    string = input()
 
 
    
    zeroCount = string.count("0")
 
    if zeroCount == 1:
        print("BOB")
        continue
 

    if zeroCount %2 == 0:
        print("BOB")
    else:
        print("ALICE")