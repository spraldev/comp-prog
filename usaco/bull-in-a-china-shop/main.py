N, K = 0, 0


ideal_portrate = []
pices = []


def render_2d_list(list_2d):
    """-- used for debugging"""

    for row in list_2d:
        for item in row:
            print(item, end=" ")
        print()

with open("bcs.in", "r") as file:
    N, K = list(map(int, file.readline().strip().split()))
    

    ideal_portrate = [["."] * N for _ in range(N)]
    pices = [[["."] * N for _ in range(N)] for _ in range(K)]

    for i in range(N):
        line = list(file.readline().strip())
        for j in range(N):
            ideal_portrate[i][j] = line[j]

    for k in range(K):
        for i in range(N):
            line = list(file.readline().strip())
            for j in range(N):
                pices[k][i][j] = line[j]

def offset_horizontal(lst, offset):
    if not lst:
        return lst
    if offset > 0:
        offset = offset % len(lst[0])
        return [row[-offset:] + row[:-offset] for row in lst]
    elif offset < 0:
        offset = abs(offset) % len(lst[0])
        return [row[offset:] + row[:offset] for row in lst]
    return lst

def offset_vertical(lst, offset):
    if not lst:
        return lst
    if offset > 0:
        offset = offset % len(lst)
        return lst[offset:] + lst[:offset]
    elif offset < 0:
        offset = abs(offset) % len(lst)
        return lst[-offset:] + lst[:-offset]
    return lst

def check_match(x_ofset1, y_ofset1, pice1, pice2, x_ofset2, y_ofset2):
    newpic1 = offset_horizontal(pice1, x_ofset1)
    newpic1 = offset_vertical(newpic1, y_ofset1)

    newpic2 = offset_horizontal(pice2, x_ofset2)
    newpic2 = offset_vertical(newpic2, y_ofset2)

    stitched_piece = [["."] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if newpic1[i][j] == "#" or newpic2[i][j] == "#":
                stitched_piece[i][j] = "#"
            else:
                stitched_piece[i][j] = "."

    for i in range(N):
        for j in range(N):
            if stitched_piece[i][j] != ideal_portrate[i][j]:
                return False

    return True



def find_ofset_ranges(pice):
    neg_x_arr = []
    pos_x_arr = []
    neg_y_arr = []
    pos_y_arr = []

    for i in range(N):
        for j in range(N):
            if pice[i][j] == "#":
                neg_x_arr.append(j)

    neg_x_ofset = min(neg_x_arr) if neg_x_arr else 0

    for i in range(N):
        for j in range(N - 1, -1, -1):
            if pice[i][j] == "#":
                pos_x_arr.append(N - j - 1)

    pos_x_ofset = min(pos_x_arr) if pos_x_arr else 0

    for i in range(N):
        for j in range(N):
            if pice[j][i] == "#":
                neg_y_arr.append(j)

    neg_y_ofset = min(neg_y_arr) if neg_y_arr else 0

    for i in range(N):
        for j in range(N - 1, -1, -1):
            if pice[j][i] == "#":
                pos_y_arr.append(N - j - 1)

    pos_y_ofset = min(pos_y_arr) if pos_y_arr else 0

    return (neg_x_ofset, pos_x_ofset,  pos_y_ofset, neg_y_ofset)






res = []

for i in range(K):
    pice1 = pices[i]

    pice1_ofset_ranges = find_ofset_ranges(pice1)

    for j in range(K):
        pice2 = pices[j]

        pice2_ofset_ranges = find_ofset_ranges(pice2)

        for k in range(-pice1_ofset_ranges[0], pice1_ofset_ranges[1] + 1):
            for l in range(-pice1_ofset_ranges[2], pice1_ofset_ranges[3] + 1):
                for m in range(-pice2_ofset_ranges[0], pice2_ofset_ranges[1] + 1):
                    for n in range(-pice2_ofset_ranges[2], pice2_ofset_ranges[3] + 1):
                        if check_match(k, l, pice1, pice2, m, n):
                            res.append((i + 1, j + 1))
                    


final_res = list(set([x for x in res if x[0] != x[1] and x[0] < x[1]]))

print(final_res)

with open("bcs.out", "w") as file:
    file.write(str(final_res[0][0]) + " " + str(final_res[0][1]))