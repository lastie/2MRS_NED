# This file will fill out all the blank areas with the coordinates above. Also, it will only contain the lines that have the category 'G'. Finally, the whole list will be reindexed.#

with open ("NED_search_indexed.txt", "r") as myfile:
	mylist = myfile.readlines()

listoflist = []
for line in mylist:
	listoflist.append(line.split("|"))

# Now that I've read everything into a list of list, I need to fill in the blanks with all the galaxy names. And then if the category of this line reads G then it should be appended to the galaxy list.


galaxylist = []
for index, line in enumerate(listoflist):
	if line[1] == '                              ':
		line[1] = linetemp
	else:
		linetemp = line [1]
	galaxylist.append(line)

#With the blank area replaced by actual names#
with open ("everything_noblank.txt", "w") as output:
	for line in galaxylist:
		templine = line
		for index, entry in enumerate(line):
			if type(entry) != str:
				templine[index] = str(entry)
		#print (type(templine))
		output.write("|".join(templine))


#Finally, the galaxylist will be indexed and saved to an indexed txt file that's different from the one above, where the index will indicate where the element originally is.

galaxyonly = []
for line in galaxylist:
	if line[6] == "G     ":
		galaxyonly. append(line)

with open ("galaxyonly.txt", "w") as output2:
	for line in galaxyonly:
		templine = line
		for index, entry in enumerate(line):
			if type(entry) != str:
				templine[index] = str(entry)
		#print (type(templine))
		output2.write("|".join(templine))

# Reindex the galaxies.
galaxyonly_reindex = []
j = 1

for line in galaxyonly:
	line[0] = j
	galaxyonly_reindex.append(line)
	j += 1

# Write the reindexed galaxies to another file:
with open ("galaxyonly_reindex.txt", "w") as output:
	for line in galaxyonly_reindex:
		templine = line
		for index, entry in enumerate(line):
			if type(entry) != str:
				templine[index] = str(entry)
		output.write("|".join(templine))
