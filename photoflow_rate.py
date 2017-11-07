#! /usr/bin/env python2

#from __future__ import print_function
import os
import shutil
import subprocess 
from gi.repository import GExiv2

exif = None

#select input images from current directory
image_extensions = [".jpg", ".png", ".bmp"]

def file_exists(filename):
	return os.path.exists(filename)
 
def make_dir(path):
  if os.path.isdir(path): return
  try:
    os.mkdir(path)
  except:
    print "Failed to make dir " + str(path)
    pass



def get_images(dir):
  print("Scanning " + dir)
  allImages = []
  for i in os.listdir(dir):
    b, e = os.path.splitext(i)
    if e.lower() not in image_extensions: continue
    allImages.append(dir + "/" + i)
  allImages.sort()
  return allImages



base_dir = os.getcwd()
base_name = os.path.basename(base_dir)
dest_dir = os.path.join(base_dir, base_name)


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

if not os.path.isdir(os.path.join(base_dir, "favorites")): 
    print("No favorites folder")
    quit()

make_dir(dest_dir)

for p in get_images(base_dir + "/meh"):
    exif = GExiv2.Metadata(p)
    exif.set_tag_long('Xmp.xmp.Rating', 3)
    exif.save_file(p)

copytree("meh/", dest_dir)


favorite_images = [ os.path.basename(i).upper() for i in get_images(base_dir + "/favorites") ]

for p in get_images(base_dir + "/good"):
    exif = GExiv2.Metadata(p)
    name = os.path.basename(p).upper()
    if name in favorite_images:
        exif.set_tag_long('Xmp.xmp.Rating', 5)
        print(name + " 5") 
    else:
        exif.set_tag_long('Xmp.xmp.Rating', 4)
        print(name + " 4") 
    exif.save_file(p)


copytree("good/", dest_dir)










