cowchars = input()
word = input()

arr = [-1]
res = []
wordArr = list(word)

for i in range(len(wordArr)):
    let = wordArr.pop(0)
    index = cowchars.index(let)
    
    if index > arr[-1]:
        arr.append(index)
        if arr[0] == -1:
            arr.pop(0)
    else:
        new_string = cowchars
        for j in range(len(arr)):
            new_string = new_string[:arr[j]] + new_string[arr[j]].upper() + new_string[(arr[j] + 1):]
        res.append(new_string)
        arr = [index]

    
    
#print(res)
print(len(res) + 1)
