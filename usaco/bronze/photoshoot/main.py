n = int(input())
cows = input()
newStr = ""
anws = 0

def count_segments(s):
    if not s:
        return 0
    
    segments = 1  
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            segments += 1
    return segments



for i in range(0, len(cows), 2):
    pair = cows[i:i+2]

    if pair == "GH":
        newStr += "A"
    elif pair == "HG":
        newStr += "B"

print(count_segments(newStr) -1  if count_segments(newStr) % 2 == 0 and newStr[0] == "A" else count_segments(newStr))