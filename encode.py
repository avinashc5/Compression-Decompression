import sys
import re
import os

fileext = ".txt"

found = re.search(fileext + "$", sys.argv[1])
if not found:
	print("Invalid file extension")
	exit(1)

if not os.path.isfile(sys.argv[1]):
	print("File does not exist")
	exit(1)

def findnumbers(filename):
	strnumbers = []
	with open(filename) as f:
		while True:
			line = f.readline()
			if not line:
				break
			strnumbers = strnumbers + re.findall("\d+", line)
	numbers = []
	for number in strnumbers:
		numbers.append(int(number))
	return numbers
	

numbers = findnumbers(sys.argv[1])

words = []

with open(sys.argv[1]) as f:
	while True:
		line = f.readline()
		if not line:
			break
		line = line.strip()
		words = words + re.findall('[a-zA-Z]+', line)

count = {}

for word in words:
	if word in count:
		count[word] = count[word] + 1
	else:
		count[word] = 1

dictionary = {}

MINLEN = 3
MINCOUNT = 3

number = 0
for word in count.keys():
	if word not in dictionary and count[word] >= MINCOUNT and len(word) >= MINLEN:
		while number in numbers:
			number = number + 1
		dictionary[number] = word
		number = number + 1

wholetext = ''

with open(sys.argv[1]) as f:
	keys = list(dictionary.keys())
	values = list(dictionary.values())

	while True:
		line = f.readline()
		if not line:
			break
		line = line.replace('\n', '')
		for word in values:
			line = re.sub(r'^' + word + r'$', str(keys[values.index(word)]), line)
			line = re.sub(r'^' + word + r'([^0-9])', str(keys[values.index(word)]) + r'\g<1>', line)
			line = re.sub(r'([^0-9])' + word + r'([^0-9])', r'\g<1>' + str(keys[values.index(word)]) + r'\g<2>', line)
			line = re.sub(r'([^0-9])' + word + r'$', r'\g<1>' + str(keys[values.index(word)]), line)
			
		
		wholetext = wholetext + line + '\n'

print(dictionary)
print(len(dictionary))

newfile = re.sub('.txt', '.new', sys.argv[1])

with open(newfile, 'w') as f:
	for i in range(len(dictionary)):
		f.write(str(keys[i]) + ' ' + str(values[i]) + ' ')
	f.write('\n')
	f.write(wholetext)
				
				
	