with open("name_url.txt", "r") as myfile:
	mylist = myfile.readlines()

#print (mylist[:10])

listoflist = []

for line in mylist:
	line = line.replace('\'', '').replace('\n','')
	listoflist.append(line.split("|"))

#print (listoflist[:10])

url_list = open("url_list.txt", "w")
no_spec = open("no_spec.txt", "w")
urlstr = []
url = []
#t = 0

for line in listoflist:
	#print (line[0])
	#print (line[1])
	#print (type(line[0]))
	#print (type(line[1]))
	if line[1] == "[]":
		no_spec.write(line[0])
		no_spec.write("\n")
	else:
		#print (line[1])
		urlstr = line[1].replace("[",'').replace(']','').replace('\n','')
		url = urlstr.split(", ")
		for elem in url:
			url_list.write(str(elem).replace('\'','').replace('[','').replace(']',''))
			url_list.write('\n')
	#t +=1
	#if t == 20:
		#break
		

url_list.close()
no_spec.close()