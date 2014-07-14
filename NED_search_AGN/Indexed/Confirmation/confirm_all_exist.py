with open ("2MRS_NED_test.txt") as myfile1:
	ref = myfile1.readlines()

with open ("galaxyonly.txt") as myfile2:
	source = myfile2.readlines()

entry = 0
j = 0 # A tally used for testing purpose
k = 0 # A tally used for keeping unmatching entries

unmatched_coor = open ("unmatched_coor.txt","w")

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
		unmatched_coor.write(refstr)
		unmatched_coor.write("\n")
		#print (refstr, 'does not match.')
		k +=1
	#j += 1
	#if j == 200:
		#break

unmatched_coor.close()
print ('There are {0} matched entries, {1} unmatched entries.'. format(entry, k))
