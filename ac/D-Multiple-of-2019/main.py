S = input()

if len(S) < 4:
    print(0)
    exit()


pref_sum = [0]

for i in range(len(S) - 3):
    substring = S[i:i+4]
    print(substring)
    if int(substring) % 2019 == 0:
        pref_sum.append(pref_sum[-1] + 1)

print(pref_sum)