num_people = 0
num_milks = 0

party = []
sick = []


with open("badmilk.in", "r") as f:
    num_people, num_milks, num_entries, num_sick = map(int, f.readline().split())
    for i in range(num_entries):
        party.append(list(map(int, f.readline().split())))
    for i in range(num_sick):
        sick.append(list(map(int, f.readline().split())))



contaminated_milks = []

for i in range(len(sick)):
    milks = [x[1] for x in party if x[2] < sick[i][1] and x[0] == sick[i][0]]

    contaminated_milks = list(set(contaminated_milks) & set(milks) if contaminated_milks else milks)




max_meds = 0

for i in range(len(contaminated_milks)):
    milk = contaminated_milks[i]
    meds = 0


    already_drank  = []

    for j in range(len(party)):
        if party[j][1] == milk and party[j][0] not in already_drank:
            meds += 1
            already_drank.append(party[j][0])

    if meds > max_meds:
        max_meds = meds


with open("badmilk.out", "w") as f:
    f.write(str(max_meds))