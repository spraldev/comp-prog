# 2 dgits

ste = set()

for i in range(10, 100):
    strn = str(i)

    if int(strn[0])**2 < 10 and int(str(int(strn[0])**2) + strn[1]) % 9 == 0:
        print(strn)

    if int(strn[1])**2 < 10 and int(strn[0] + str(int(strn[1])**2)) % 9 == 0:
        print(strn)

    if int(strn[0])**2 < 10 and int(strn[1])**2 < 10 and int(str(int(strn[0])**2) + str(int(strn[1])**2)) % 9 == 0:
        print(strn)


# 3 digits



for i in range(100, 1000):
    strn = str(i)

    if int(strn[0])**2 < 10 and int(strn[1])**2 < 10 and int(strn[2])**2 < 10 and int(str(int(strn[0])**2) + str(int(strn[1])**2) + str(int(strn[2])**2)) % 9 == 0:
        print(strn)
    
    if int(strn[0])**2 < 10 and int(str(int(strn[0])**2) + str(strn[1]) + str(strn[2])) % 9 == 0:
        print(strn)

    if int(strn[1])**2 < 10 and int(str(strn[0]) + str(int(strn[1])**2) + str(strn[2])) % 9 == 0:
        print(strn)

    if int(strn[2])**2 < 10 and int(str(strn[0]) + str(strn[1]) + str(int(strn[2])**2)) % 9 == 0:
        print(strn)

    if int(strn[0])**2 < 10 and int(strn[1])**2 < 10 and int(str(int(strn[0])**2) + str(int(strn[1])**2) + str(strn[2])) % 9 == 0:
        print(strn)

    if int(strn[0])**2 < 10 and int(strn[2])**2 < 10 and int(str(int(strn[0])**2) + str(strn[1]) + str(int(strn[2])**2)) % 9 == 0:
        print(strn)

    if int(strn[1])**2 < 10 and int(strn[2])**2 < 10 and int(str(strn[0]) + str(int(strn[1])**2) + str(int(strn[2])**2)) % 9 == 0:
        print(strn)

    if int(strn[0])**2 < 10 and int(strn[1])**2 < 10 and int(strn[2])**2 < 10 and int(str(int(strn[0])**2) + str(int(strn[1])**2) + str(int(strn[2])**2)) % 9 == 0:
        print(strn)


    if int(strn[0])**2 < 10 and int(strn[1])**2 < 10 and int(strn[2])**2 < 10 and int(str(int(strn[0])**2) + str(int(strn[1])**2) + str(int(strn[2])**2)) % 9 == 0:
        print(strn)