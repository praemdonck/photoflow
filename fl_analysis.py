#! /usr/bin/env python2


from gi.repository import GExiv2
import os

image_extensions = [".jpg"]

def get_images(dir):
  print("Scanning " + dir)
  allImages = []
  for i in os.walk(dir):
    for file in i[2]:
      b, e = os.path.splitext(file)
      if e.lower() not in image_extensions: continue
      allImages.append(os.path.join(i[0], file))

  allImages.sort()
#for i in allImages:
#    print  i #os.path.basename(i)
  return allImages



base_dir = os.getcwd()
image_list = get_images(base_dir)
buckets = [0] * 301
for i in image_list:
  exif = GExiv2.Metadata(i)
#print  exif['Exif.Image.Model'] 
  if exif.get('Exif.Image.Model') == "NIKON D80" or exif.get('Exif.Image.Model') == "NIKON D7200":
    fl=int(exif.get_focal_length())
    buckets[fl] += 1
    print i + ' Focal Length: ' + str(fl)


for i in range(301):
  print "FL %d -> %d" % (i, buckets[i])
