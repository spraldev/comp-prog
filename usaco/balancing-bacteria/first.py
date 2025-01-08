## This is the initial solution that I came up with. It passes 10/15 test cases, before it fails due to time limit exceeded.
## The solution is O(n^2)

N = int(input())
bacteria = list(map(int, input().split()))

copy = bacteria.copy()


def apply_stuff(dif, multiplier=1):
    for i in range(N - 1, -1, -1):
        if dif < 0:
            copy[i] -= dif * -1 * multiplier
        else:
            copy[i] += dif * multiplier
        if dif > 0:
            dif -= 1
        else:
            dif += 1
        
        if dif == 0:
            break

    return copy


count = 0


for i in range(N):
    if copy[i] < 0:
        count += abs(copy[i])


        apply_stuff((N-i), abs(copy[i]))

        

    else:
        count += abs(copy[i])

        apply_stuff((-(N-i)), abs(copy[i]))

        

    if copy == [0] * N:
        break

print(count)