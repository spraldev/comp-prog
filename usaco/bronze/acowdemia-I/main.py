import bisect

N, L = list(map(int, input().split()))
papers = list(map(int, input().split()))

L = min(N, L)

appearence_dict = {}

for i in range(N):
    if papers[i] not in appearence_dict:
        appearence_dict[papers[i]] = 1
    else:
        appearence_dict[papers[i]] += 1

for i in range(min(appearence_dict.keys()), max(appearence_dict.keys()) + 2):
    if i not in appearence_dict:
        appearence_dict[i] = 0

papers.sort()
res_arr = []


for key, value in appearence_dict.items():
    curPapers = len(papers) - bisect.bisect_left(papers, key)

    papersRequired = key - curPapers if key > curPapers else 0

    if curPapers + appearence_dict.get(key-1, 0) >= key and papersRequired <= L:
        res_arr.append(key)


print(max(res_arr))

