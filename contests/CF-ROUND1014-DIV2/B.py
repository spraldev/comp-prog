for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    

    if a.count('1') == 0:
        print('YES')
        continue

    comp1_capacity = len(b[1::2])
    comp1_total = a[0::2].count('1') + b[1::2].count('1')
    

    comp2_capacity = len(b[0::2])
    comp2_total = a[1::2].count('1') + b[0::2].count('1')
    
    if comp1_total <= comp1_capacity and comp2_total <= comp2_capacity:
        print("YES")
    else:
        print("NO")
