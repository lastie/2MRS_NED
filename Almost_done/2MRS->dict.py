# !!!Caution
# Just remember that the key for the dictionary is a string, so when typed in you have to make it a strong, or add ''.

# 2MRS+ NED -> dict
with open ("2MRS.txt","r") as myfile:
	mylist = myfile.readlines()

listoflist = []

for line in mylist: #Line is a list, elements in the line are strings.
	listoflist.append(line.split())

ned = {}
coor = ''
z = 0

# Write the 2MRS data file into a dictionary with key as the string RA +' ' +Dec, and the value is the z value. 

for line in listoflist:
	if line[26] == 'N':
		z = float(line[24]) / 299792.458
		if line[2][0] != "-":
			line[2] = '+' + line[2]
		coor = str(line[1]) + ' ' + str(line[2]) 
		ned.update({coor:z})

with open ("ned.txt", "w") as output:
	output.write(str(ned))

#print (ned['284.28232 -78.47256'])

# 11375 results -> dict

with open ("allgalaxies_indexed.txt","r") as myfile:
	mylist = myfile.readlines()

listoflist = []

for line in mylist: #Line is a list, elements in the line are strings.
	listoflist.append(line.split("|"))

mygalaxies = {}
coor = ''
z = 0

# Caution for special case again. Some NED search galaxy matches do not have redshift. We will save these to a separate list & file.

for line in listoflist:
	coor = line[1].rstrip()
	z = float(line[7]) / 299792.458
	mygalaxies.update({coor:z})

with open ("mygalaxies.txt", "w") as output:
	output.write(str(mygalaxies))




		
