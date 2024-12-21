n = 0;
lines = [];
score1 = 0;
score2 = 0;
score3 = 0;

shells = [1, 0, 0];

with open("shell.in", "r") as f:
    lines  = f.read().split("\n");
    n = int(lines[0]);



for i in range(n):
    a = int(lines[i + 1].split()[0]) - 1;
    b = int(lines[i + 1].split()[1]) - 1;
    g = int(lines[i + 1].split()[2]) - 1;

    temp = shells[a];
    shells[a] = shells[b];
    shells[b] = temp;
    
    if shells[g] == 1:
        score1 += 1;


shells = [0, 1, 0];

for i in range(n):
    a = int(lines[i + 1].split()[0]) - 1;
    b = int(lines[i + 1].split()[1]) - 1;
    g = int(lines[i + 1].split()[2]) - 1;


    temp = shells[a];
    shells[a] = shells[b];
    shells[b] = temp;
    
    if shells[g] == 1:
        score2 += 1;



shells = [0, 0, 1];



for i in range(n):
    a = int(lines[i + 1].split()[0]) - 1;
    b = int(lines[i + 1].split()[1]) - 1;
    g = int(lines[i + 1].split()[2]) - 1;

    temp = shells[a];
    shells[a] = shells[b];
    shells[b] = temp;
    
    if shells[g] == 1:
        score3 += 1;

with open("shell.out", "w") as f:
    f.write(str(max(score1, score2, score3)));
