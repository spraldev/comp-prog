a = 0
b = 0
c = 0
d = 0

distance = 0

with open("paint.in", "r") as f:
    content = f.read()
    content = content.split("\n")
    a = int(content[0].split(" ")[0])
    b = int(content[0].split(" ")[1])
    c = int(content[1].split(" ")[0])
    d = int(content[1].split(" ")[1])
    print([a,b,c,d])

# Not Overlap



if ((a > c and a < d) and (b > c and b < d)):
    distance = d - c
elif ((c > a and c < b) and (d > a and d < b)):
    distance = b - a
elif not ((c < b and c > a) or (d > a and d < b)):
    dist1 = b - a
    dist2 = d - c

    print("hi")
    
    distance = dist1 + dist2
# Overlap
else:
    minim = min([a,b,c,d])
    maxim = max([a,b,c,d])



    distance = maxim - minim


with open("paint.out", "w") as f:
    f.write(str(distance))
    print(f"\n{distance}\n")