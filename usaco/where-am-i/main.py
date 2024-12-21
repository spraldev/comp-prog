s = "";

with open("whereami.in", "r") as f:
    f.readline().strip()
    s = f.readline().strip()


def consecutive_combinations(lst, n):
    return [lst[i:i + n] for i in range(len(lst) - n + 1)]

answer = 0

for i in range(1, 101):
    substrings = consecutive_combinations(s, i)
    substrings_set = set(substrings)

    if len(substrings) == len(substrings_set):
        answer = i
        break

with open("whereami.out", "w") as f:
    f.write(str(answer) + "\n")
