file = input("Enter file name: ")
fhandle = open(file)
counts=dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
    
print(counts)


bigCount = None
bigWord = None

for word,count in counts.items():
    if bigCount == None or count>bigCount:
        bigWord = word
        bigCount = count

print(bigWord,bigCount)