import re

file = open("./resources/regex_sum_135221.txt")

numbers = list()

for line in file :
	search = re.findall("\d+", line)
	if len(search) > 0 :
		for num in search :
			numbers.append(int(num))

sum = sum(numbers)
count = len(numbers)

print(sum)
