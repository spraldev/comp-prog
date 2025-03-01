def next_non_empty_line():
    line = input().strip()
    while line == "":
        line = input().strip()
    return line

def gen_rots(stamp):
    rots = [stamp]
    for _ in range(3):
        rots.append([list(reversed(col)) for col in zip(*rots[-1])])
    return rots

t = int(next_non_empty_line())
for _ in range(t):
    n = int(next_non_empty_line())
    painting = [list(next_non_empty_line()) for _ in range(n)]
    k = int(next_non_empty_line())
    stamp = [list(next_non_empty_line()) for _ in range(k)]
    rots = gen_rots(stamp)

    capped = []

    for rot in rots:
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                valid = True
                for l in range(k):
                    for m in range(k):
                        if rot[l][m] == '*' and painting[i+l][j+m] != '*':
                            valid = False
                            break
                    if not valid:
                        break

                if valid:
                    for l in range(k):
                        for m in range(k):
                            if rot[l][m] == '*' and painting[i + l][j + m] == "*":
                                capped.append((i + l, j + m))

    capped = list(set(capped))

    P = True

    for i in range(n):
        for j in range(n):
            if painting[i][j] == "*" and (i, j) not in capped:
                P = False
                break

    print("YES" if P else "NO")
                
