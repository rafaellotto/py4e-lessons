file = open("./resources/mbox-short.txt")
count = 0
for line in file :
    if not line.startswith("From ") : continue
    print(line.split()[1])
    count = count + 1

print("There were %d lines in the file with From as the first word" % count)
