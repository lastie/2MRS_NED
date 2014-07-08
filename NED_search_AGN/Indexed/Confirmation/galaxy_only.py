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

#test output#
with open ("test.txt", "w") as output:
	for line in galaxylist:
		templine = line
		for index, entry in enumerate(line):
			if type(entry) != str:
				templine[index] = str(entry)
		output.write(templine)
		output.write("\n")


#Finally, the galaxylist will be indexed and saved to an indexed txt file that's different from the one above, where the index will indicate where the element originally is.

galaxyindexed = []
