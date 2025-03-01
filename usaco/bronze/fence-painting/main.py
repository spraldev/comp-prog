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

if b < c or d < a:
    distance = (b - a) + (d - c)
    
else:
    distance = (max(a, b,c,d) - min(a, b, c, d))

with open("paint.out", "w") as f:
    f.write(str(distance))
    print(f"\n{distance}\n")