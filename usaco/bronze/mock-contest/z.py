from string import ascii_lowercase


N, F = map(int, input().split())
nstring = input()





def count_moos(string):
    final_res = []
    MooDict = {}
    for i in range(len(string) - 2):
        three_char_string = string[i:i+3]

        if three_char_string[0] != three_char_string[1] and three_char_string[1] == three_char_string[2]:
            if three_char_string in MooDict:
                MooDict[three_char_string] += 1

                if MooDict.get(three_char_string, 0) >= F:
                    final_res.append(three_char_string)
            else:
                MooDict[three_char_string] = 1

    return final_res


arr = []


for i in range(len(nstring)):
    for letter in ascii_lowercase:
        new_string = nstring[:i] + letter + nstring[i+1:]
        if new_string == nstring:
            continue
        arr += count_moos(new_string)

print(len(set(arr)))
for i in sorted(list(set(arr))):
    print(i)

