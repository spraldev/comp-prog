N, K = 0, 0
words = []

with open("word.in", "r") as f:
    N, K = map(int, f.readline().strip().split())
    words = f.readline().strip().split()


final_arr  = []
temp_arr = []

def check_len(arr):
    return sum([len(i) for i in arr])

for i in range(N):
    if check_len(temp_arr) + len(words[i]) <= K:
        temp_arr.append(words[i])
    else:
        final_arr.append(temp_arr)
        temp_arr = [words[i]]

if len(temp_arr) > 0:
    final_arr.append(temp_arr)


with open("word.out", "w") as f:
    for i in final_arr:
        f.write(" ".join(i) + "\n")