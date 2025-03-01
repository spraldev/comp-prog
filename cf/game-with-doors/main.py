
T = int(input())

for _ in range(T):
    interval1 = tuple(map(int, input().split()))
    interval2 = tuple(map(int, input().split()))

    maxL = max(interval1[0], interval2[0])
    maxR = max(interval1[1], interval2[1])
    minR = min(interval1[1], interval2[1])
    minL = min(interval1[0], interval2[0])

    cont = minR - maxL + 2

    if cont <= 0:
        print(1)
        continue

    # print(minL, maxL, minR, maxR)
    # print(cont)


    if minR == maxR:
        cont -= 1
    if minL == maxL:
        cont -= 1

    # print(cont)



    print(cont)