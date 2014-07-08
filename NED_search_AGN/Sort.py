#Sort the list of objects with respect to activity type

with open ("NED_search_indexed.txt") as myfile:
	mylist = myfile.readlines()

# Reads the file into a list of list, same as before
listoflist = []

i = 0
for line in mylist:
	listoflist.append(line.split("|"))

from operator import itemgetter
sorted(listoflist, key = itemgetter(8))
editedlist = listoflist

# Save the edited list to an output file
with open ("NED_search_sorted.txt", "w") as output:
	for line in editedlist:
		templine = line
		for index, entry in enumerate(line):
			if type(entry) == int:
				templine[index] = str(entry)
		output.write("|".join(templine)) # For some reason, when you print things in a for loop, they automatically appear in the file to on separate lines, as in a new line sign is automatically inserted.


