fname = input("Enter file name: ")
fh = open("./resources/" + fname + ".txt")
numbers = []

for line in fh :
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence: ") : continue
    pos = line.find(" ")
    num = float(line[pos:])
    numbers.append(num)

total = 0

for number in numbers :
    total = total + number

avg = total / len(numbers)

print("Average spam confidence:", avg)
