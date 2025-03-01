import sys

#sys.stdout = open("output.txt", "w")

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
        if i in conj:
            return True
    return False



def solve():
    N, C, P = map(int, input().split())

    trans = []
    intrans = []
    nouns = []
    conj = []

    for i in range(N):
        wordStr = input().split()
        if wordStr[1] == "noun":
            nouns.append(wordStr[0])
        elif wordStr[1] == "transitive-verb":
            trans.append(wordStr[0])
        elif wordStr[1] == "intransitive-verb":
            intrans.append(wordStr[0])
        elif wordStr[1] == "conjunction":
            conj.append(wordStr[0])

    intransArr = []

    #limit both intransitive verbs and nouns by available nouns and max sentences
    max_intrans = min(len(intrans), len(nouns))
    intrans = intrans[:max_intrans]

    for i in range(len(intrans)):
        intransArr.append(nouns[i] + " " + intrans[i])


    unUsedNouns = nouns[len(intrans):]

    

    temp = [[]]

    if trans: 
        for i in range(len(trans)):
            # make a list of sentences with i iintransitive verbs (i sentences), and evenly distribute the nouns, and append that to temp
            nouns_copy = unUsedNouns.copy()
            nouns_per_sentence = len(unUsedNouns) // (i + 1)

            if nouns_per_sentence < 2:
                break

            newTemp = trans[:i + 1]

            
            for j in range(i + 1):
                newTemp[j] = nouns_copy[0] + " " + newTemp[j]
                nouns_copy.pop(0)

            nouns_per_sentence -= 1

            for j in range(i + 1):
                for k in range(nouns_per_sentence):
                    newTemp[j] += " " + nouns_copy[0]
                    nouns_copy.pop(0)

            temp.append(newTemp)

            leftOverNouns = nouns_copy.copy()

            for i in range(len(newTemp)):
                if leftOverNouns:
                    newTemp[i] += " " + leftOverNouns.pop(0)
                else:
                    break


            temp.append(newTemp)


            

    arrs = temp

    # print(arrs)

    arrs.sort(key=lambda x: count_words(x), reverse=True)

    final_str_res = []


    
    
    for i in range(len(arrs)):
        arr = arrs[i] + intransArr
        result = []
        conj_copy = conj.copy()
        copyy = arr.copy()

        i = 0
        p_copy = P
        c_copy = C

        while i < len(arr):
            if p_copy == 0 or c_copy == 0:
                break

            if i == len(arr) - 1:
                words_i = arr[i].split()

                if len(words_i) > 2:
                    newArrI = words_i[0] + " " + words_i[1] + " " + ", ".join(words_i[2:])
                else:
                    newArrI = arr[i]

                result.append(newArrI + ".")
                break
            
            if conj_copy:
                words_i = arr[i].split()
                words_i_plus_1 = arr[i + 1].split()

                if len(words_i) > 2:
                    newArrI = words_i[0] + " " + words_i[1] + " " + ", ".join(words_i[2:])
                else:
                    newArrI = arr[i]

                if len(words_i_plus_1) > 2:
                    newArrIPlusOne = words_i_plus_1[0] + " " + words_i_plus_1[1] + " " + ", ".join(words_i_plus_1[2:])
                else:
                    newArrIPlusOne = arr[i + 1]

                if not is_conj(newArrI, conj_copy) and not is_conj(newArrIPlusOne, conj_copy):
                    result.append(newArrI + " " + conj_copy.pop(0) + " " + newArrIPlusOne + ".")
                    i += 2
                    p_copy -= 1
                    c_copy -= newArrI.count(",") + newArrIPlusOne.count(",")
                else:
                    result.append(arr[i] + ".")
                    i += 1
                    p_copy -= 1
                    c_copy -= arr[i].count(",")
            else:
                result.append(arr[i] + ".")
                i += 1
                p_copy -= 1
                c_copy -= arr[i].count(",")
        
        arr = result

        if count_commas(arr) <= C and len(arr) <= P:
            final_str_res.append(" ".join(arr))

    return max(final_str_res, key=lambda x: len(x.split())) if final_str_res else ""

resArr = []

for i in range(T):
    result = solve()
    if result:
        resArr.append(result)
    else:
        resArr.append("")

for i in resArr:
    print(len(i.split()))
    print(i)
