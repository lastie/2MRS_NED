with open ("galaxies.txt","r") as myfile:
	mylist = myfile.readlines()

listoflist = []

for line in mylist:
	listoflist.append(line.split("|"))

editedlist = []
i = 1

for line in listoflist:
	line[0] = i
	editedlist.append(line)
	i +=1

with open ("allgalaxies_indexed.txt", "w") as output:
	for line in editedlist:
		templine = line
		for index, entry in enumerate(line):
			if type(entry) == int:
				templine[index] = str(entry)
		output.write("|".join(templine))

