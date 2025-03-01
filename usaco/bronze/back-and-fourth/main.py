from itertools import combinations_with_replacement

barn1 = 1000
barn2 = 1000

barn1_buckets = []
barn2_buckets = []

with open("backforth.in", "r") as f:
    barn1_buckets = list(map(int, f.readline().split()))
    barn2_buckets = list(map(int, f.readline().split()))

anws = []
otherAnws = []

for i in range(len(barn1_buckets)):
    copy1 = barn1_buckets.copy()
    copy2 = barn2_buckets.copy()

    barn1 -= barn1_buckets[i]
    barn2 += barn1_buckets[i]

    copy2.append(copy1[i])
    copy1.pop(i)

    for j in range(len(copy2)):
        barn1_j = barn1
        barn2_j = barn2
        copy1j = copy1.copy()
        copy2j = copy2.copy()

        barn2_j -= copy2j[j]
        barn1_j += copy2j[j]

        copy1j.append(copy2j[j])
        copy2j.pop(j)

        for k in range(len(copy1j)):
            barn1_k = barn1_j
            barn2_k = barn2_j
            copy1k = copy1j.copy()
            copy2k = copy2j.copy()

            barn1_k -= copy1k[k]
            barn2_k += copy1k[k]

            copy2k.append(copy1k[k])
            copy1k.pop(k)

            for l in range(len(copy2k)):
                barn1_l = barn1_k
                barn2_l = barn2_k
                copy1l = copy1k.copy()
                copy2l = copy2k.copy()

                barn2_l -= copy2l[l]
                barn1_l += copy2l[l]

                copy1l.append(copy2l[l])
                copy2l.pop(l)

                if copy1l not in anws:
                    anws.append(copy1l)
                
                if barn1_l not in otherAnws:
                    otherAnws.append(barn1_l)

                barn1_l = barn1_k
                barn2_l = barn2_k

                copy1l = copy1k.copy()
                copy2l = copy2k.copy()



            # Restore `barn1` and `barn2` for the next iteration of `k`
            barn1_k = barn1_j
            barn2_k = barn2_j

            copy1k = copy1j.copy()
            copy2k = copy2j.copy()

        # Restore `barn1` and `barn2` for the next iteration of `j`
        barn1_j = barn1
        barn2_j = barn2

        copy1j = copy1.copy()
        copy2j = copy2.copy()


    # Restore `barn1` and `barn2` for the next iteration of `i`
    barn1 = 1000
    barn2 = 1000

    copy1 = barn1_buckets.copy()
    copy2 = barn2_buckets.copy()



with open("backforth.out", "w") as f:
    f.write(str(len(otherAnws)) + "\n")
