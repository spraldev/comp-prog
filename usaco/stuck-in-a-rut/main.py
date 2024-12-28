N = int(input())


cows = []
final_dict = {}

for i in range(N):
    cow = input().split()

    cows.append((cow[0], int(cow[1]), int(cow[2])))


northCows = [cow for cow in cows if cow[0] == 'N']
eastCows = [cow for cow in cows if cow[0] == 'E']


for cow in cows:
    final_dict[cow] = 0


for i in range(len(eastCows)):
    newNorthCows = [cow for cow in northCows if cow[1] > eastCows[i][1] and cow[2] < eastCows[i][2]]
    #newNorthCows.sort(key=lambda x: x[1])

    eatMin = -1

    for j in range(len(newNorthCows)):
        xDiff = newNorthCows[j][1] - eastCows[i][1]
        yDiff = eastCows[i][2] - newNorthCows[j][2]

        newEastCows = [cow for cow in eastCows if cow[1] < newNorthCows[j][1] and cow[2] > newNorthCows[j][2]]
        newEastCows.sort(key=lambda x: x[2])

        alreadyStopped = False

        for k in range(len(newEastCows)):
            xDiff2 = newEastCows[k][1] - newNorthCows[j][1]
            yDiff2 = newNorthCows[j][2] - newEastCows[k][2]

            if eastCows[i] == newEastCows[k]:
                continue


            if yDiff2 < xDiff2 and newEastCows[k][2] < eastCows[i][2]:
                alreadyStopped = True
                break

        if xDiff > yDiff and not alreadyStopped:
            squaresEaten = xDiff
            if squaresEaten < eatMin or eatMin == -1:
                eatMin = squaresEaten

    if eatMin != -1:
        final_dict[(eastCows[i][0], eastCows[i][1], eastCows[i][2])] = eatMin
    else:
        final_dict[(eastCows[i][0], eastCows[i][1], eastCows[i][2])] = 'Infinity'



for i in range(len(northCows)):
    # list of eastcows, with x < northCows[i][1] and y > northCows[i][2]
    newEastCows = [cow for cow in eastCows if cow[1] < northCows[i][1] and cow[2] > northCows[i][2]]
    newEastCows.sort(key=lambda x: x[2])

    eatMin = -1


    for j in range(len(newEastCows)):
        xDiff = northCows[i][1] - newEastCows[j][1] 
        yDiff = newEastCows[j][2] - northCows[i][2]

        # list of all north cows, with x > newEastCows[j][1] and y < newEastCows[j][2]
        newNorthCows = [cow for cow in northCows if cow[1] > newEastCows[j][1] and cow[2] < newEastCows[j][2]]
        newNorthCows.sort(key=lambda x: x[1])

        alreadyStopped = False

        for k in range(len(newNorthCows)):
            xDiff2 = newNorthCows[k][1] - newEastCows[j][1]
            yDiff2 = newEastCows[j][2] - newNorthCows[k][2]

            if northCows[i] == newNorthCows[k]:
                continue

            #if the cow is already stopped, and the point of stopping is before the current cow, then break

            if xDiff2 > yDiff2 and newNorthCows[k][1] < northCows[i][1]:
                alreadyStopped = True
                break
        

        if yDiff > xDiff and not alreadyStopped:
            squaresEaten = yDiff
            if squaresEaten < eatMin or eatMin == -1:
                eatMin = squaresEaten

    if eatMin != -1:
        final_dict[(northCows[i][0], northCows[i][1], northCows[i][2])] = eatMin
    else:
        final_dict[(northCows[i][0], northCows[i][1], northCows[i][2])] = 'Infinity'


for cow in cows:
    print(final_dict[cow])