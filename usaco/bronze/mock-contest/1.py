T = int(input())

for _ in range(T):
    N = int(input())
    count = 0
    strN = str(N)

    if len(strN) == 1:
        print(0)
        continue

    for i in range(len(strN) -1):
        if i > 0:
            count += int("5" * i)

    lwer_bound = (int("4" * (len(strN) - 1) + "5") )
    upper_bound = (int( "4" + "9" * (len(strN) - 1)) )

    if N < lwer_bound:
        count += 0
    elif N > upper_bound:
        count += int("5" * (len(strN) - 1))
    else:
        count += N - lwer_bound + 1

    print(count)