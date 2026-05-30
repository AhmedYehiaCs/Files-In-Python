filename=input("Enter file name: ")
try:
    fhand = open(filename)
except:
    print("File cannot be opened",filename)
    quit()

for line in fhand :
    line = line.rstrip()
    print(line)