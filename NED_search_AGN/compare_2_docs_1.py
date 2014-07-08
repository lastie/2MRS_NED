with open ("2MRS_NED_test.txt") as myfile1:
	ref = myfile1.readlines()

with open ("NED_search_300_bar.txt") as myfile2:
	source = myfile2.readlines()

entry = 0
for line in ref:
	#print line
	refstr = str(line).rstrip('\r\n')
	i = 0
	for lline in source:
		#print (coor)
		srcstr = str(lline)
		#print refstr, srcstr
		#print srcstr.find(refstr)
		if srcstr.find(refstr) != -1:
			i = 1
			entry +=1
			break
	if i == 0:
		print (line, 'does not match.')

print ('There are {0} matched entries'. format(entry))



