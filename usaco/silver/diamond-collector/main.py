import sys

sys.stdin = open('diamond.in', 'r')
sys.stdout = open('diamond.out', 'w')   


N, K = map(int, input().split())
Diamonds = [int(input()) for _ in range(N)]
Diamonds.sort()

i = 0
j = 1

intervals = []

while j < N - 1 and i < N - 1:
    if Diamonds[j] - Diamonds[i] <= K:
        intervals.append((i, j, j - i + 1))

        j += 1
    else:
        i += 1
        j = i + 1

intervals.append((0, 0, 1))
intervals.append((1, 1, 1))

intervals.sort(key=lambda x: x[2], reverse=True)
two_intervals = intervals[:2]
two_intervals.sort(key=lambda x: x[0])


def check_overlap(interval1, interval2):
    return interval1[1] > interval2[0] and interval1[0] < interval2[1]

# if they overlap

if check_overlap(two_intervals[0], two_intervals[1]):
    print(two_intervals[0][0] - two_intervals[1][1] + 1)
else:
    print(two_intervals[0][2] + two_intervals[1][2])