for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = sum(a)
    odd_count = sum(1 for x in a if x % 2 == 1)
    
    if odd_count == 0 or odd_count == n:
        print(max(a))
    else:
        print(total - (odd_count - 1))
