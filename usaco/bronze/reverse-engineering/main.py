testCases = int(input())
dummy = input()

for _ in range(testCases):
    N, M = map(int, input().split())
    tests = [input.split() for _ in range(N)]

    p = True

    indicies = list(range(N))

    while len(indicies) > 1:
        i = indicies.pop()

        oneGroup = set()
        twoGroup = set()

        oneOutput = ""
        twoGroup = ""


        for test in tests:
            if test[0][i] == '0':
                if oneGroup == "":
                    oneGroup = test[1]

                if oneGroup != test[1]:
                    break

                oneGroup.add(test[1])

            else:
                if twoGroup == "":
                    twoGroup = test[1]

                if twoGroup != test[1]:
                    break

                twoGroup.add(test[1])

        

        if len(oneGroup) == 1 and len(twoGroup) == 1:
            print("LIE")
            p = False
            break

    if p:
        print("OK")

    dummy = input()