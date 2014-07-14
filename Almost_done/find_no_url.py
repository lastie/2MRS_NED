with open ("name_url.txt", "r") as myfile:
	mylist = myfile.readlines()

listoflist = []
for line in mylist:
	line = line.rstrip('\'')
	listoflist.append(line.split("["))

print (listoflist[1:10])
url_output = open ("just_url.txt","w")
no_url = open ("no_url.txt","w")

for line in listoflist:
	if line[1] != ']':
		url_output.write(line[1])
	else:
		no_url.write(line[0])



