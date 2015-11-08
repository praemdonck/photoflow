#! /usr/bin/env python2

import os
import subprocess 

image_extensions = [".jpg", ".png", ".bmp"]


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


negatives_base_dir         = "/media/pablo/Media/Fotos/Negatives"
negatives_links_base_dir   = "/media/pablo/Media/Fotos/Negatives_links"
dropbox_negatives_base_dir = "/home/pablo/Dropbox/Photos/Negatives"

base_dir = os.getcwd()
base_name = os.path.basename(base_dir)
negatives_target_dir = os.path.join(negatives_base_dir, base_name)

#Move files to negative folder
command = ["mv"]
command.append(base_dir)
command.append(negatives_target_dir)
print command
subprocess.call(command)

#Create negative links
negatives_ln_path = os.path.join(negatives_links_base_dir, base_name)
make_dir(negatives_ln_path)

image_list = get_images(negatives_target_dir)
for i in image_list:
  image_dir, image_name = os.path.split(i)
  link_name = os.path.join(negatives_ln_path, image_name)
  link_target = os.path.relpath(image_dir, negatives_ln_path)
  link_target = os.path.join(link_target, image_name)
  print link_name + " -> " + link_target
  os.symlink(link_target, link_name)


#Create link to negatives in Dropbox folder
link_name = os.path.join(dropbox_negatives_base_dir, base_name)
os.symlink(negatives_target_dir, link_name)
print link_name + " -> " + negatives_target_dir
