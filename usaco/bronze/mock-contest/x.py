from decimal import Decimal, ROUND_HALF_UP

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return int(int(Decimal(n * multiplier).to_integral_value(rounding=ROUND_HALF_UP)) / multiplier)

def bessie_round(x):
    return round_half_up(x, -len(str(x)))

def chain_round(x):
    num = x
    pwr = len(str(x))

    for i in range(1, pwr + 1):
        num = round_half_up(num, -i)

    
    return num

T = int(input())

for _ in range(T):
    N = int(input())
    count = 0
    olddig = 0
    
    for i in range(N):
        if bessie_round(i + 1) != chain_round(i + 1):
            count += 1

            print(i + 1, i -1) if len(str(i + 1)) != olddig else None
            olddig = len(str(i + 1))

    print(count)


    counter = 0