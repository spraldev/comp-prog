def inter_area(s1, s2) -> int:
	bl_a_x, bl_a_y, tr_a_x, tr_a_y = s1[0], s1[1], s1[2], s1[3]
	bl_b_x, bl_b_y, tr_b_x, tr_b_y = s2[0], s2[1], s2[2], s2[3]
     
    

	return ((min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x)) * (
		min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y)
	) if (min(tr_a_x, tr_b_x) - max(bl_a_x, bl_b_x)) * (
		min(tr_a_y, tr_b_y) - max(bl_a_y, bl_b_y)
	) > 0 else 0) if bl_a_x < tr_b_x and bl_a_y < tr_b_y and bl_b_x < tr_a_x and bl_b_y < tr_a_y else 0

def get_overlap_vertices(s1, s2) -> tuple:
    bl_x = max(s1[0], s2[0])
    bl_y = max(s1[1], s2[1])
    tr_x = min(s1[2], s2[2])
    tr_y = min(s1[3], s2[3])
    if bl_x < tr_x and bl_y < tr_y:
        return (bl_x, bl_y, tr_x, tr_y)
    else:
        return ()
    
def area(bl_x: int, bl_y: int, tr_x: int, tr_y: int) -> int:
	length = tr_y - bl_y
	width = tr_x - bl_x
	return length * width


paper = tuple(map(int, input().split()))
rect_1 = tuple(map(int, input().split()))
rect_2 = tuple(map(int, input().split()))


overlap_1 = get_overlap_vertices(paper, rect_1)
overlap_2 = get_overlap_vertices(paper, rect_2)
overlap_area_1 = inter_area(paper, rect_1)
overlap_area_2 = inter_area(paper, rect_2)

# print(overlap_1, overlap_2)

overlap_aera = inter_area(overlap_1, overlap_2) if overlap_1 and overlap_2 else 0

final_aera = overlap_area_1 + overlap_area_2 - overlap_aera


# print(area(paper[0], paper[1], paper[2], paper[3]), final_aera, overlap_aera, overlap_area_1, overlap_area_2)

# print(overlap_area_1)

if final_aera < area(paper[0], paper[1], paper[2], paper[3]):
    print("YES")
else:
    print("NO")