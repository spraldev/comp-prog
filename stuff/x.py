
# T = list(input())

def fast(S):


    # calculate the n-1th triangular number
    tri = ((len(S) -1) * (len(S))) // 2

    count = 0
    anws = tri


    for i in range(len(S)):
        if i == len(S) - 1:
            break

        if S[i] == S[i + 1]:
            count += 1
        else:
            anws -= (count + 1) if count > 0 else 0
            count = 0

    anws -= (count + 1) if count > 0 else 0

    return anws

def slow(S):
    ste = set()

    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            cop = S.copy()
            
            temp = cop[i]
            cop[i] = cop[j]
            cop[j] = temp
            
            ste.add(tuple(cop))
            
    return len(ste)



print(slow(list("abbxvc")))
print(fast(list("abbxvc")))

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# failed = False
# passed = False

# # test
# for i in range(len(alphabet)):
#     for j in range(len(alphabet)):
#         for k in range(len(alphabet)):
#             for l in range(len(alphabet)):
#                 for m in range(len(alphabet)):
#                     for n in range(len(alphabet)):
#                         if fast([alphabet[i], alphabet[j], alphabet[k], alphabet[l], alphabet[m], alphabet[n]]) != slow([alphabet[i], alphabet[j], alphabet[k], alphabet[l], alphabet[m], alphabet[n]]):
#                             print("Failed")
#                             print([alphabet[i], alphabet[j], alphabet[k], alphabet[l], alphabet[m], alphabet[n]])
#                             print(fast([alphabet[i], alphabet[j], alphabet[k], alphabet[l], alphabet[m], alphabet[n]]), slow([alphabet[i], alphabet[j], alphabet[k], alphabet[l], alphabet[m], alphabet[n]]))
#                             failed = True
#                         else:
#                             print("Passed")
#                             print([alphabet[i], alphabet[j], alphabet[k], alphabet[l], alphabet[m], alphabet[n]])
#                             print(fast([alphabet[i], alphabet[j], alphabet[k], alphabet[l], alphabet[m], alphabet[n]]), slow([alphabet[i], alphabet[j], alphabet[k], alphabet[l], alphabet[m], alphabet[n]]))
#                             passed = True
                        
#                         if passed and failed:
#                             exit()

                        


