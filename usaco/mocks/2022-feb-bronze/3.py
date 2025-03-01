import itertools

N = int(input())

cubes = [input() for _ in range(4)]

perms = list(itertools.permutations(cubes))

for _ in range(N):
    word = input()
    p = False

    for perm in perms:
        perm_p = True
        i = 0

        for cube in perm:
            if i >= len(word):
                break


            if word[i] not in cube:
                perm_p = False
                break
            i += 1

        if perm_p:
            p = True
            break

    


    print("YES" if p else "NO")

        

        