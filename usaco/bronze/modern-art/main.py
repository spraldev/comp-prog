N = 0
art = [[]]

with open("art.in", "r") as f:
    N = int(f.readline())
    art = [list(map(int, list(f.readline().strip()))) for _ in range(N)]
    
def render_2d_list(list_2d):
    """-- used for debugging"""

    for row in list_2d:
        for item in row:
            print(item, end=" ")
        print()

nums = []

for i in range(N):
    for j in range(N):
        if art[i][j] not in nums and art[i][j] != 0:
            nums.append(art[i][j])

def get_only_num(num):
    # given a number, return a smaller portion of art, that contains the "territory" of that number
    # the terriorty is defined by the maximum rectangle that contains all the cells with the given number

    # find the top left and bottom right corners of the rectangle
    top_left = (N, N)
    bottom_right = (0, 0)

    for i in range(N):
        for j in range(N):
            if art[i][j] == num:
                top_left = (min(top_left[0], i), min(top_left[1], j))
                bottom_right = (max(bottom_right[0], i), max(bottom_right[1], j))

    # create a new 2d list with the territory
    territory = [[0 for _ in range(bottom_right[1] - top_left[1] + 1)] for _ in range(bottom_right[0] - top_left[0] + 1)]

    for i in range(top_left[0], bottom_right[0] + 1):
        for j in range(top_left[1], bottom_right[1] + 1):
            territory[i - top_left[0]][j - top_left[1]] = art[i][j]

    return territory


def check_num(num):
    for Num in nums:
        Num_arr = get_only_num(Num)

        if Num == num:
            continue

        for i in range(len(Num_arr)):
            for j in range(len(Num_arr[i])):
                if Num_arr[i][j] == num:
                    return False


    return True

anws = 0

for i in range(len(nums)):
    if check_num(nums[i]):
        anws += 1

with open("art.out", "w") as f:
    f.write(str(anws))