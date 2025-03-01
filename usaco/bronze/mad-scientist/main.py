n = 0
a = []
b = []


with open("breedflip.in", "r") as f:
    n = int(f.readline().strip())
    b = list(f.readline().strip())
    a = list(f.readline().strip())

count = 0
rangee = True

for i in range(len(a)):
    if a[i] != b[i] and rangee:
        count += 1
        rangee = False

    if a[i] == b[i] and not rangee:
        rangee = True

with open("breedflip.out", "w") as f:
    f.write(str(count))