file = open("./resources/mbox-short.txt")

senders = {}
for line in file :
    if not line.startswith("From ") : continue
    sender = line.split()[1]
    if sender not in senders :
        senders[sender] = 1
    else :
        senders[sender] += 1

max = 0
user = ""
for sender in senders :
    if senders[sender] > max :
        max = senders[sender]
        user = sender

print(user, max)
