with open ("2MRS_NED_z042.txt", "r") as myfile:
	data=myfile.read().replace('-', ' -')
	data1=data.replace('+', ' +')
print data1

f = open("test.txt", "w")
f.write(data1)
f.close
