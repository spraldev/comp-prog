n = 0

mildred = [7] * 100
elsie = [7] * 100
bessie = [7] * 100

with open("measurement.in", "r") as f:
    n = int(f.readline().strip())

    tuples = []

    for i in range(n):
        day, cow, change = f.readline().strip().split()
        day = int(day)
        change = int(change)

        tuples.append((day, cow, change))

    tuples.sort()

    for i in range(n):
        day, cow, change = tuples[i]

        if cow == "Mildred":
            for j in range(day-1, 100):
                mildred[j] += change
        elif cow == "Elsie":
            for j in range(day-1, 100):
                elsie[j] += change
        elif cow == "Bessie":
            for j in range(day-1, 100):
                bessie[j] += change

final_count = 0

def max_with_duplicates(a, b, c):
    max_value = max(a, b, c)

    if a == b == c:
        return ([a, b, c], ["Mildred", "Elsie", "Bessie"])
    elif a == max_value and b == max_value:
        return ([a, b], ["Mildred", "Elsie"])
    elif a == max_value and c == max_value:
        return ([a, c], ["Mildred", "Bessie"])
    elif b == max_value and c == max_value:
        return ([b, c], ["Elsie", "Bessie"])
    else:
        if max_value == a:
            return ([a], ["Mildred"])
        elif max_value == b:
            return ([b], ["Elsie"])
        elif max_value == c:
            return ([c], ["Bessie"])

final_count = 0
current_display = [7, 7, 7]
current_display_names = ["Mildred", "Elsie", "Bessie"]


for i in range(100):


    if current_display != max_with_duplicates(mildred[i], elsie[i], bessie[i])[0] and current_display_names != max_with_duplicates(mildred[i], elsie[i], bessie[i])[1]:
        final_count += 1
        current_display = max_with_duplicates(mildred[i], elsie[i], bessie[i])
        current_display_names = max_with_duplicates(mildred[i], elsie[i], bessie[i])[1]

with open("measurement.out", "w") as f:
    f.write(str(final_count))
    