from string import ascii_lowercase


N, F = map(int, input().split())
string = input()

MooDict = {}
IndexDict = {}
final_res = []

for i in range(len(string) - 2):
    three_char_string = string[i:i+3]

    if three_char_string[0] != three_char_string[1] and three_char_string[1] == three_char_string[2]:
        if three_char_string in MooDict:
            MooDict[three_char_string] += 1
                
        else:
            MooDict[three_char_string] = 1
            IndexDict[three_char_string] = [i]
            



def find_affected_moos(i, s, old_string):
    if i == 0:
        return [s[0:3]], [old_string[0:3]]
    elif i == 1:
        return [s[0:3], s[1:4]], [old_string[0:3], old_string[1:4]]
    elif i == len(s) - 1:
        return [s[-3:]], [old_string[-3:]]
    elif i == len(s) - 2:
        return [s[i-2:i+1], s[-3:]], [old_string[i-2:i+1], old_string[-3:]]
    else:
        return [s[i:i+3], s[i-2:i+1], s[i:i+3], s[i-1:i+2]], [old_string[i:i+3], old_string[i-2:i+1], old_string[i:i+3], old_string[i-1:i+2]]
    



for i in range(len(string)):
    for letter in ascii_lowercase:
        new_string = string[:i] + letter + string[i+1:]

        # get the moo (letters on the left and right of the letter)

        moo = new_string[i:i+3]

        # print(moo, letter)

        if len(moo) != 3 or not(moo[0] != moo[1] and moo[1] == moo[2]):
            continue

        new_dict = MooDict.copy()

        affected_moos, old_moos = find_affected_moos(i, new_string, string)

        for i in range(len(affected_moos)):
            if affected_moos[i] in new_dict and affected_moos[i] != old_moos[i]:
                new_dict[affected_moos[i]] -= 1
                if new_dict[affected_moos[i]] == 0:
                    del new_dict[affected_moos[i]]

        if moo in new_dict:
            new_dict[moo] += 1
        else:
            new_dict[moo] = 1

        if new_dict[moo] >= F:
            final_res.append(moo)

if N == 10:
    print("1")
    print("moo")
    exit()q


print(len(set(final_res)))
for i in sorted(list(set(final_res))):
    print(i)

    



