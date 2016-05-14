#! /usr/bin/env python2

import os
import subprocess 
from time import sleep

image_extensions = [".jpg", ".png", ".bmp", ".mov"]


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
  for i in os.walk(dir):
    for file in i[2]:
      b, e = os.path.splitext(file)
      if e.lower() not in image_extensions: continue
      allImages.append(os.path.join(i[0], file))

  allImages.sort()
#for i in allImages:
#    print  i #os.path.basename(i)
  return allImages


#negatives_base_dir         = "/media/pablo/Media/Fotos/Negatives"
negatives_base_dir         = "/home/pablo/Pictures/Negatives"
#negatives_links_base_dir   = "/media/pablo/Media/Fotos/Negatives_links"
negatives_links_base_dir   = "/home/pablo/Pictures/Negatives_links"
dropbox_negatives_base_dir = "/home/pablo/Dropbox/Photos/Negatives"
favorites_base_dir = "/home/pablo/Pictures/Favorites"

base_dir = os.getcwd()
base_name = os.path.basename(base_dir)
negatives_target_dir = os.path.join(negatives_base_dir, base_name)
favorites_target_dir = os.path.join(favorites_base_dir, base_name)

#Move files to negative folder
command = ["mv"]
command.append(base_dir)
command.append(negatives_target_dir)
print command
os.chmod(negatives_base_dir, 0755)
sleep(1)
subprocess.call(command)

command = ["chmod"]
command.append("-R")
command.append("555")
command.append(negatives_target_dir)
print command
subprocess.call(command)

#sleep(2)
os.chmod(negatives_base_dir, 0555)

#Create negative links
negatives_ln_path = os.path.join(negatives_links_base_dir, base_name)
make_dir(negatives_ln_path)

#Create favorites directory
make_dir(favorites_target_dir)

image_list = get_images(negatives_target_dir)
for i in image_list:
  image_dir, image_name = os.path.split(i)
  link_name = os.path.join(negatives_ln_path, image_name)
  link_target = os.path.relpath(image_dir, negatives_ln_path)
  link_target = os.path.join(link_target, image_name)
  print link_name + " -> " + link_target
  os.symlink(link_target, link_name)

os.chmod(negatives_ln_path, 0555)

#Create link to negatives in Dropbox folder
link_name = os.path.join(dropbox_negatives_base_dir, base_name)
os.symlink(negatives_target_dir, link_name)
print link_name + " -> " + negatives_target_dir
