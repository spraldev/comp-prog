from bisect import bisect_left



num_farms, num_queries = list(map(int, input().split()))
closing_times = list(map(int, input().split()))
visitm_times = list(map(int, input().split()))


final_list = []
new_list = []

for j in range(num_farms):
    new_list.append(closing_times[j] - visitm_times[j])

new_list.sort()

def countGreater(arr, n, k):
    l = 0
    r = n - 1
 
    leftMax = n

    while (l <= r):
        m = int(l + (r - l) / 2)
 
        if (arr[m] > k):
            leftMax = m
            r = m - 1
 
        else:
            l = m + 1
 
    return (n - leftMax)


for i in range(num_queries):
    query = list(map(int, input().split()))

    if countGreater(new_list, len(new_list), query[1]) >= query[0]:
        final_list.append("YES")
    else:
        final_list.append("NO")


for i in final_list:
    print(i)