import sys

sys.stdin = open("lemonade.in")
sys.stdout = open("lemonade.out", "w+")

n = int(input())
cows = sorted(list(map(int, input().split())), reverse=True)

def solve():
    for i in range(n):
        if cows[i] < i:
            print(i)
            return
    print(n)


solve()
