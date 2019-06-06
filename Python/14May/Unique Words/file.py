
words = []
uniqueWords = words

with open("words.txt", "r") as fp:
    for line in fp:
        words.extend(line.split())

words.sort()
uniqueWords.sort()
print(', '.join(words))
print("\n",', '.join(uniqueWords))

'''i = 0
words.sort()
uniqueWords.extend(words[i])
for i in range(len(words)):
    
    if words[i] == uniqueWords[i]:
        i += 1
    else:
        uniqueWords.extend(words[i])
        i += 1

i = 0
for i in range(len(uniqueWords)):
    print(uniqueWords[i], end="")
    i = i + 1
    
'''