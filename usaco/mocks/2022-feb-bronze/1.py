for _ in range(int(input())):
    #range = 0...sum(a)
    n = int(input())
    a = list(map(int, input().split()))

    sun = sum(a)
    res = 0
    

    if max(a) == 0:
        print(0)
        continue


    for i in range(1, sun+1,):
        if len(a) - sun/i > 0 and int(len(a) - sun/i) == len(a) - sun/i:
            h = 0
            p = False
            for j in range(len(a)):
                h += a[j]
                if h > i and j +1 < sun/i:
                    p = True
                    break

            if not p:
                res = int(len(a) - sun/i)
                break

    print(res)

    




    