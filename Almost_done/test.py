from astroquery.ned import Ned

image_list = []
image_list += Ned.get_image_list('NGC_5128', item = 'spectra')

print (image_list)