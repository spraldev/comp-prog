view = [[0 for _ in range(2000)] for _ in range(2000)]
area = 0
billboard1 = 0;
billboard2 = 0;

with open("billboard.in", "r") as f:
    content = f.read().splitlines()

    x1, y1, x2, y2 = map(int, content[0].split())

    for i in range(2000):
        for j in range(2000):
            if(x1 <= j-1000 and j-1000 <= x2) and (y1 <= i-1000 and i-1000 <= y2):
                view[i][j] = 1
            else:
                view[i][j] = 0

    billboard1 = (x2 - x1) * (y2 - y1)

    x1, y1, x2, y2 = map(int, content[2].split())

    for i in range(2000):
        for j in range(2000):
            if(x1 <= j-1000 and j-1000 <= x2) and (y1 <= i-1000 and i-1000 <= y2):
                view[i][j] = 1
            else:
                view[i][j] = 0

    billboard2 = (x2 - x1) * (y2 - y1)

    x1, y1, x2, y2 = map(int, content[1].split())

    for i in range(2000):
        for j in range(2000):
            if(x1 <= j-1000 and j-1000 <= x2) and (y1 <= i-1000 and i-1000 <= y2):
                if(view[i][j] == 1):
                    area += 1


print((billboard2 + billboard1) - area)











    
            

