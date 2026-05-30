fhandle = open("str.txt","r")

# print(fhandle)

# print("Hello\nWorld")

count= 0
fhandle.seek(0)
for line in fhandle:
    line = line.rstrip()
    # count += 1
    # print(line.rstrip())
    # if line.startswith("Ahmed"):
        # print(line)


    # if not line.startswith("Ahmed"):
    #     continue
    print(line)

# print("List count",count,"\n-------------------------------------------------------")
# print(fhandle.read())
# fhandle2 = open("str2.txt","r")
# print(fhandle2.read())


