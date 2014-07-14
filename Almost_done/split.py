with open ("name_url.txt", "r") as f:
	thelist = f.readlines()

listoflist = []
for line in thelist:
	line = line.rstrip("\n:']")
	print (line)
	listoflist.append(line.split("["))

print (listoflist[:10])