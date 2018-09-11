file = open("mbox-short.txt")

hour = ""
counts = {}
for line in file :
    if not line.startswith("From ") : continue
    pos = line.find(":")
    hour = line[pos - 2 : pos]
    if hour not in counts :
        counts[hour] = 1
    else :
        counts[hour] += 1

t = list(counts.items())
t.sort()

for h, i in t :
    print(h,i)
