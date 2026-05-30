# Use the file name mbox-strings.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    indx = line.find(" ")
    num=line[indx:26]
    num =float(num)
    total=float(total)
    count=float(count)
    total = total + num
    while count < 27:
        count+=1
print("Average spam confidence:",total/count)
