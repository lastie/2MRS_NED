with open ("galaxyonly_reindex.txt", "r") as myfile:
	mylist = myfile.readlines()

listoflist = []

for line in mylist:
	listoflist.append(line.split("|"))

temp = listoflist[0][1]

duplicate = []
for line in listoflist[1:]:
	if line[1] == temp:
		print ('We have a duplicate of {0}.'.format(temp))
		duplicate.append(temp)
	temp = line[1]

duplicateset = set(duplicate)
print ('We have {0} duplicates.'.format(len(duplicateset)))
print (len(duplicate))

with open ("duplicate.txt", "w") as output:
	for line in duplicateset:
		templine = line
		for index, entry in enumerate(line):
			if type(entry) != str:
				templine[index] = str(entry)
		output.write(templine)
		output.write("\n")

