import sys
import os
import re

fileext = '.new'

found = re.search(fileext + "$", sys.argv[1])
if not found:
	print("Invalid file extension")
	exit(1)

if not os.path.isfile(sys.argv[1]):
	print("File does not exist")
	exit(1)

with open(sys.argv[1], 'r') as f:
	dictionary = {}
	line = f.readline().strip()
	line = line.split(' ')
	keys = line[::2]
	values = line[1::2]
	for i in range(len(keys)):
		dictionary[int(keys[i])] = values[i]

	originaltext = ''
	while True:
		line = f.readline()
		if not line:
			break
		line = line.replace('\n', '')
		for number in keys:
			line = re.sub(r'^' + number + r'$', values[keys.index(number)], line)
			line = re.sub(r'^' + number + r'([^0-9])', values[keys.index(number)] + r'\g<1>', line)
			line = re.sub(r'([^0-9])' + number + r'([^0-9])', r'\g<1>' + values[keys.index(number)] + r'\g<2>', line)
			line = re.sub(r'([^0-9])' + number + r'$', r'\g<1>' + values[keys.index(number)], line)
		originaltext = originaltext + line + '\n'

with open('trial.txt', 'w') as f:
	f.write(originaltext)