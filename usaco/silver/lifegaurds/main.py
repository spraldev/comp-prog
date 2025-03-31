import sys

sys.stdin = open('lifeguards.in', 'r')
sys.stdout = open('lifeguards.out', 'w')


N = int(input())
lifegaurds = [tuple(map(int, input().split())) for _ in range(N)]

lifegaurds.sort(key=lambda x: x[0])

total_time = 0

cur_interval_start = lifegaurds[0][0]
cur_interval_end = lifegaurds[0][1]

for i in range(1, N):
    if lifegaurds[i][0] > cur_interval_end:
        total_time += cur_interval_end - cur_interval_start
        cur_interval_start = lifegaurds[i][0]
        cur_interval_end = lifegaurds[i][1]
    else:
        cur_interval_end = max(cur_interval_end, lifegaurds[i][1])

total_time += cur_interval_end - cur_interval_start

# find the min alone time between all lifegaurds, in o(n)

min_alone_time = float('inf')

for i in range(N):
    # we will do this, by looking at the left and right lifegaurds, due to the nature of the sorted intervals
    left_lifeguard = lifegaurds[i-1] if i > 0 else None
    right_lifeguard = lifegaurds[i+1] if i < N-1 else None

    if left_lifeguard and right_lifeguard:
        # how much would the left cut into the cur
        left_cut = max(0, left_lifeguard[1] - lifegaurds[i][0])
        # how much would the right cut into the cur
        right_cut = max(0, lifegaurds[i][1] - right_lifeguard[0])

        alone_time = (lifegaurds[i][1] - lifegaurds[i][0]) - (left_cut + right_cut)
    elif left_lifeguard:
        left_cut = max(0, left_lifeguard[1] - lifegaurds[i][0])
        alone_time = (lifegaurds[i][1] - lifegaurds[i][0]) - left_cut
    elif right_lifeguard:
        right_cut = max(0, lifegaurds[i][1] - right_lifeguard[0])
        alone_time = (lifegaurds[i][1] - lifegaurds[i][0]) - right_cut
    
    min_alone_time = min(min_alone_time, alone_time)

print(total_time - min_alone_time)
