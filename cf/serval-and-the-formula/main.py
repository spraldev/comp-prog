powers_of_2 = []
power = 1
while power <= 10**18:
    powers_of_2.append(power)
    power *= 2



for _ in range(int(input())):
    x, y = map(int, input().split())

    for i in range(len(powers_of_2)):
        for j in range(i, len(powers_of_2)):
            if powers_of_2[i] < x or powers_of_2[j] < y:
                continue

            if powers_of_2[i] - x == powers_of_2[j] - y:
                print(powers_of_2[i] - x)
                break

        else:
            continue
        break

    else:
        print(-1)