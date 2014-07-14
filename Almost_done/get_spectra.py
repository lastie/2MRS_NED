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

image_list = []
full_list = []

#print ('here')
from astroquery.ned import Ned

#print ('okay')

output = open("download.txt", "w")

#print (len(gnames))

for name in gnames:
	image_list = Ned.get_image_list(name, item = 'spectra')
	full_list += image_list

print ("full_list done")

for item in image_list:
	output.write(item)

print ('at the end')
#print (len(image_list))

output.close()