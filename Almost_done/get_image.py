with open ("gnames.txt", "r") as myfile:
	mylist = myfile.readlines()

#print (mylist[:10])

name = []
for item in mylist:
	name.append(item.rstrip("\n"))

#print (name[:10])

from astroquery.ned import Ned

image_list = {}
url = []

for entry in name:
	url = Ned.get_image_list(entry, item = 'spectra')
	image_list.update({entry:url})

nomatch = []
import urllib

for name, url in image_list:
	if url == []:
		nomatch.append(name)
	else:
		urllib.urlretrieve (url)
