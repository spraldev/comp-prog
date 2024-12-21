badSquare = []
goodSquare = []


with open ("billboard.in", "r") as fin:
    badSquare = list(map(int, fin.readline().strip().split()))
    goodSquare = list(map(int, fin.readline().strip().split()))


def inter_area(s1, s2) -> int:
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]

	return (min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x)) * (
		min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y)
	)


def inter_lens(s1, s2) -> int:
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]

	return ((min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x)),  (
		min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y)
	))

def side_lengths(s1) -> int:
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]

	return (tr_a_x - bl_a_x, tr_a_y - bl_a_y)




intersection_lengts = inter_lens(badSquare, goodSquare)


#print(intersection_lengts)

print(side_lengths(badSquare), intersection_lengts)


if intersection_lengts[0] not in side_lengths(badSquare) and intersection_lengts[1] not in side_lengths(badSquare):
    with open("billboard.out", "w") as fout:
        fout.write(str(side_lengths(badSquare)[0] * side_lengths(badSquare)[1]))
    exit()
# if the y cordinfates of the good square lie within the y cordinates of the bad square or the x coordinates of the good square lie within the x coordinates of the bad square
elif (goodSquare[1] >= badSquare[1] and goodSquare[3] <= badSquare[3]) or (goodSquare[0] >= badSquare[0] and goodSquare[2] <= badSquare[2]):
    with open("billboard.out", "w") as fout:
        fout.write(str(side_lengths(badSquare)[0] * side_lengths(badSquare)[1]))
    exit()

else:
    with open("billboard.out", "w") as fout:
        fout.write(str(side_lengths(badSquare)[0] * side_lengths(badSquare)[1] - intersection_lengts[0] * intersection_lengts[1]))
    exit()
