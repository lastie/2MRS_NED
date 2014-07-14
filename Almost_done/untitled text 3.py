#! /usr/bin/env python
with open ("2MRS.txt", "r") as myfile:
	mylist = myfile.readlines()

listoflist = []

for line in mylist:
	listoflist.append(line.split())

gnames = []

#print (len(listoflist))

for line in listoflist:
	#print (line[26])
	if line[26] == 'N':
		gnames.append(str(line[28]))


with open ("gnames.txt", "w") as output:
	for name in gnames:
		output.write(name)
		output.write("\n")
