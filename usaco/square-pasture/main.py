sq1 = []
sq2 = []
with open("square.in", "r") as f:
    content = f.read().split("\n")

    for line in content:
        line.split()

    sq1 = list(map(int, content[0].split()))
    sq2 = list(map(int, content[1].split()))


print(sq1)
print(sq2)


sidelenx = abs(sq1[2] - sq2[0])
sideleny = abs(sq1[3] - sq2[1])

sidelen2x = abs(sq2[2] - sq1[0])
sidelen2y = abs(sq2[3] - sq1[1])



sqsidelenx = abs(sq1[0] - sq1[2])
sqsideleny = abs(sq1[1] - sq1[3])

sq2sidelenx = abs(sq2[0] - sq2[2])
sq2sideleny = abs(sq2[1] - sq2[3])

print(sidelenx, sideleny, sqsidelenx, sqsideleny, sq2sidelenx, sq2sideleny)

with open("square.out", "w") as f:
    f.write(str(max(sidelenx, sideleny, sqsidelenx, sqsideleny, sq2sidelenx, sq2sideleny, sidelen2x, sidelen2y)**2))
    