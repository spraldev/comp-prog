unCensoredString = ""
badWord = ""


with open("censor.in", "r") as file:
    unCensoredString = file.readline().strip()
    badWord = file.readline().strip()

newString = ""

for i in range(len(unCensoredString)):
    if i < len(badWord):
        newString += unCensoredString[i]
        continue

    newString += unCensoredString[i]

    if newString[-len(badWord):] == badWord:
        newString = newString[:-len(badWord)] 

unCensoredString = newString



with open("censor.out", "w") as file:
    file.write(unCensoredString)