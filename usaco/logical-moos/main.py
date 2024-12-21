N, Q = list(map(int, input().split()))
Statements = list(input().split())

for i in range(len(Statements)):
    if Statements[i] == "true":
        Statements[i] = True
    elif Statements[i] == "false":
        Statements[i] = False








final_arr = []

for i in range(Q):
    copy = Statements.copy()

    query = list(input().split())

    
    del copy[int(query[0])-1:int(query[1])-1]


    resArr = []
    

    copy[int(query[0]) - 1] = True


    if eval(" ".join([str(x) for x in copy])):
        resArr.append(True)
    else:
        resArr.append(False)

    copy[int(query[0]) - 1] = False

    if eval(" ".join([str(x) for x in copy])):
        resArr.append(True)
    else:
        resArr.append(False)

    
    queryBool = True if query[2] == "true" else False

    if queryBool in resArr:
        final_arr.append("Y")
    else:
        final_arr.append("N")
    
    
    


for i in final_arr:
    print(i, end="")