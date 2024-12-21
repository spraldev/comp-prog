lines = []
params = []

with open('cowsignal.in', 'r') as f:
    file = f.read().strip()  # Read and strip any trailing newlines
    lines = file.split("\n")
    params = lines[0].split()
    lines = lines[1:]  # Skip the first line after extracting params

with open('cowsignal.out', 'w') as f:
    for index, line in enumerate(lines):  # Use enumerate to track index
        linearr = list(line)
        
        for i, char in enumerate(linearr):
            linearr[i] = char * int(params[2])  # Expand each character
        
        linestr = "".join(linearr)
        
        for i in range(int(params[2])):  # Repeat the entire line K times
            f.write(linestr)
            if index != len(lines) - 1 or i != int(params[2]) - 1:  # Correct newline handling
                f.write("\n")
