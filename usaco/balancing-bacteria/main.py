n = int(input())

bacteria = list(map(int, input().split()))


def adder_pesticide(level):
    for i in range(n):
        affect = level - i;
        bacteria[n-i-1] = bacteria[n-i-1] + affect;

def subtracter_pesticide(level):
    for i in range(n):
        affect = level - i;
        bacteria[n-i-1] = bacteria[n-i-1] - affect;

# every bacteria should be 0 after this loop

for i in range(n):
    

print(sum(bacteria))