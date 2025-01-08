
T = int(input())

def count_words(arr):
    count = 0
    for i in arr:
        count += len(i.split())
    return count

def count_commas(arr):
    count = 0
    for i in arr:
        count += i.count(",")
    return count

def is_conj(string, conj):
    for i in string.split():
        if i not in conj:
            return False
    return True



def solve():
    N, C, P = map(int, input().split())

    trans = []
    intrans = []
    nouns = []
    conj = []

    for i in range(N):
        wordStr = input().split()
        
        match wordStr[1]:
            case "noun":
                nouns.append(wordStr[0])
            
            case "transitive-verb":
                trans.append(wordStr[0])
            
            case "intransitive-verb":
                intrans.append(wordStr[0])

            case "conjunction":
                conj.append(wordStr[0])

    intransArr = []

    intrans = intrans[:min(len(intrans), P)]


    for i in range(len(intrans)):
        intransArr.append(nouns[i] + " " + intrans[i])


    unUsedNouns = nouns[len(intrans):]

    transArr = []
    arrs = []
    max_num = 0

    if intransArr: 
        for i, current_noun in enumerate(unUsedNouns[:len(intransArr)]):
            transArr.append(current_noun + " " + intransArr[i])
            
            temp = transArr.copy()
            temp_nouns = [x for x in unUsedNouns if x != current_noun]

            if temp:  
                num_nouns = len(temp_nouns) // len(temp)
                
                for j in range(len(temp)):
                    temp[j] = temp[j] + " " + ", ".join(temp_nouns[j*num_nouns:(j+1)*num_nouns])

            arrs.append(temp)
            max_num = max(max_num, count_words(temp))


    arrs.sort(key=lambda x: count_words(x), reverse=True)

    final_str = ""

    for i in range(len(arrs)):
        # check if the count of the commas is less than C
        # check if the amount of periods is valid
        # add conjunctions and periods and the intrans arr to the end of the string

        newArr = intransArr + arrs[i]
        if count_commas(newArr) <= C and len(newArr) <= P:
            conj_copy = conj.copy()
            while newArr:
                if len(newArr) == 1:
                    final_str += newArr[0] + "."
                    newArr.pop(0)
                elif not conj_copy:
                    final_str += newArr[0] + ". "
                    newArr.pop(0)
                else:
                    final_str += newArr[0] + " " + conj_copy.pop(0) + " "
                    newArr.pop(0)


            break

    return final_str

            
for i in range(T):
    result = solve()
    if result:
        print(len(result.split()))
        print(result)
    else:
        print(0)
