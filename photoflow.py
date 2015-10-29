#! /usr/bin/env python2

#from __future__ import print_function
import os
import subprocess 

#select input images from current directory
image_extensions = [".jpg", ".png", ".bmp"]
rules = { "-1" : { "operations" : ["resize", "delete"],      "folder" : "Rejected",  "max_size" : "1000", "jpg_qual" : "70" },
           "0" : { "operations" : ["none"] },
           "1" : { "operations" : ["resize", "delete"],      "folder" : "1_star",    "max_size" : "1800", "jpg_qual" : "85" },
           "2" : { "operations" : ["resize", "delete"],      "folder" : "2_star",    "max_size" : "2560", "jpg_qual" : "85" },
           "3" : { "operations" : ["resize", "delete"],      "folder" : "3_star",    "max_size" : "4000", "jpg_qual" : "85" },
           "4" : { "operations" : ["change_qual", "delete"], "folder" : "4_star",    "max_size" : "4000", "jpg_qual" : "85" },
           "5" : { "operations" : ["move"],                  "folder" : "5_star"                                             }
} 

def file_exists(filename):
	return os.path.exists(filename)
 
def make_dir(path):
  if os.path.isdir(path): return
  try:
    os.mkdir(path)
  except:
    print "Failed to make dir " + str(path)
    pass


def process_image(img, rating):
  if not file_exists(img):
    print "Cannot find file: " + str(img)
    return

  if rating not in rules: 
    print "No rules to process rating: " + str(rating)
    return

  if "none" in rules[rating]['operations']:
    print "No operations in rules for rating: " + str(rating)
    return

  if "folder" in rules[rating]:
    dest_path, filename = os.path.split(img)
    dest_path += "/" + rules[rating]["folder"]
    dest = dest_path + "/" + filename
    make_dir(dest_path)
  else:
    dest = img

  if "move" in rules[rating]["operations"]:
    os.rename(img, dest)

  if ("resize" in rules[rating]["operations"] or 
      "change_qual" in rules[rating]["operations"]):
    command = ["convert"]
    if "max_size" in rules[rating] and "resize" in rules[rating]["operations"]:
      command.append("-size")
      command.append(rules[rating]["max_size"]) 
      command.append("-resize")
      command.append(rules[rating]["max_size"])

    if "jpg_qual" in rules[rating]:
      command.append("-quality")
      command.append(rules[rating]["jpg_qual"])

    command.append(img)
    command.append(dest)
    print command
    subprocess.call(command)

  if "delete" in rules[rating]["operations"]:
    os.remove(img)




def get_images(dir):
  print("Scanning " + dir)
  allImages = []
  for i in os.listdir(dir):
    b, e = os.path.splitext(i)
    if e.lower() not in image_extensions: continue
    allImages.append(dir + "/" + i)
  allImages.sort()
  return allImages



#Set test folder
#os.chdir("/home/pablo/src/photoflow/test")
#base_dir = "/home/pablo/src/photoflow/test"
base_dir = os.getcwd()

#path = []
#for i in range(1,6):
#  path.append(base_dir + "/%d_star" % i)
#
#path.append(base_dir + "/Rejected")
#path.append(base_dir + "/Unrated")
#
#
#for p in path:


images = get_images(base_dir)

for p in images:
 #a = call(["exiv2", "-K Xmp.xmp.Rating", "-PX", p])
#temp = base_dir + "/" + p
#print call(["exiv2", "-K Xmp.xmp.Rating", "-PX", temp])
#print call(["exiv2", "-K", "Xmp.xmp.Rating", "-PX", "/home/pablo/src/photoflow/test/DSC_0530.JPG"])
  try:
    a = subprocess.check_output(["exiv2", "-K", "Xmp.xmp.Rating", "-PX", p])
    a = a.split()[3]
  except:
    print "Failed to get rating for image " + str(p)
    a = '0'
#  print call(["exiv2", "-V"])
#print call(["echo", "hello world"])
  print(p + " Rating: " + a)
  process_image(p, a)
#print a
