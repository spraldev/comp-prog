from bisect import bisect_left



num_farms, num_queries = list(map(int, input().split()))
closing_times = list(map(int, input().split()))
visitm_times = list(map(int, input().split()))


final_list = []
new_list = []

for j in range(num_farms):
    new_list.append(closing_times[j] - visitm_times[j])

def count_less_than(arr, num):

    """ 

    Returns the count of elements in 'arr' that are less than 'num'.

    """

    arr.sort()  # Sort the array in ascending order

    return bisect_left(arr, num)




for i in range(num_queries):
    query = list(map(int, input().split()))

    count = 0


    print(count_less_than(new_list, query[1]))

    for i in new_list:
        if i < query[1]:
            count += 1

    print(count)

    print("\n\n")

            

    # if count_less_than(new_list, query[1]) >= query[0]:
    if count >= query[0]:
        final_list.append("YES")

    else:
        final_list.append("NO")

for i in final_list:
    print(i)





