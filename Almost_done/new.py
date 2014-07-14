with open ("gnames2.txt", "r") as myfile:
	mylist = myfile.readlines()

#print (mylist[:10])

name = []
for item in mylist:
	name.append(item.rstrip("\n"))

#print (name[:10])

from astroquery.ned import Ned

image_list = {}
url = []
i = 5256

address = open("name_url3.txt","w")

for entry in name:
	print (i)
	url = Ned.get_image_list(entry, item = 'spectra')
	print (entry, url)
	image_list.update({entry:url})
	address.write(entry)
	address.write("|")
	address.write(str(url))
	address.write("\n")
	i +=1
	#if i == 5:
		#break

address.close()
