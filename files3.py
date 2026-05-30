inp = input("Enter File Name...")
try:
    fhandle = open(inp)
except:
    print("There is no such a file called",inp)
    quit()
myList = list()
for line in fhandle :
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    index = line.find(" ")
    number = line[index+1:]
    number = float(number)
    myList.append(number)

print(myList)
print("Average spam confidence:",sum(myList)/len(myList))