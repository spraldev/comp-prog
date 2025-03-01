for _ in range(int(input())):
    N = int(input())
    imp = list(input())

    if imp[0] == "s":
        imp[0] = "."
    
    if imp[-1] == "p":
        imp[-1] = "."

    foundS = False
    foundP = False


    for i in range(N):
        if imp[i] == "s":
            foundS = True
        elif imp[i] == "p":
            foundP = True


    print("NO" if foundP and foundS else "YES")