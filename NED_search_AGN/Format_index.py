with open ("NED_search_300_bar.txt") as myfile:
	mylist = myfile.readlines()
# mylist is a list of the whole table, with each item one of its lines as string.

listoflist = []
# listoflist is a list of the whole table, but each item is a list initself, which is a list of entries on that line.
# In each item in listoflist, the corresponding entries with respect to the list index are: 0- Row No. 1-Input coor, 2-distance from coor, 3-name, 4-RA, 5-Dec, 6-type, 7-z, 8-activity type, 9-Row No + newline.

#print (type(listoflist))
i = 0
for line in mylist:
	listoflist.append(line.split("|"))
	#print (listoflist[i])
	#i +=1
	#if i == 5:
		#break

#print (listoflist)

# In the next loop we need to change Row No. to 1-15000, and get rid of the last column.
# We also need to save our edited list to a new list.

j = 1
editedlist = []

for line in listoflist:
	#print (line)
	line.pop() #removes and returns the last item of the list
	line[0] = j
	editedlist.append(line)
	#print (editedlist[j-1])
	j +=1
	#if j == 5:
		#break

#print(editedlist)

# Save the edited list to an output file
with open ("NED_search_indexed.txt", "w") as output:
	for line in editedlist:
		templine = line
		for index, entry in enumerate(line):
			if type(entry) == int:
				templine[index] = str(entry)
		output.write("|".join(templine))
		output.write("\n")
		 # For some reason, when you print things in a for loop, they automatically appear in the file to on separate lines, as in a new line sign is automatically inserted.















