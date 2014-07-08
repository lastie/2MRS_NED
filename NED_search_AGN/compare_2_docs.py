with open ("2MRS_NED_test.txt") as myfile1:
	data = myfile1.readlines()

with open ("NED_search_AGN.txt") as myfile2:
	bulk = myfile2.readlines()


entry = 0
for line in bulk:
	str2 = str(line)
	i = 0
	for coor in data:
		str1 = str(data[i])
		if str2.find(str1):
			entry +=1
			i = 1
			break
	if i == 0:
		print (line, 'does not match.')

print ('There are {0} entries'. format(entry))



