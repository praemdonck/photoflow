#! /usr/bin/env python2
import os


image_extensions = [".jpg", ".png", ".bmp"]

def get_images_sidecar(dir):
  print("Scanning " + dir)
  allImages = []

  if not os.path.isdir(dir): 
      return allImages

  for i in os.listdir(dir):
    b, e = os.path.splitext(i)
#print(b + "   " + e)
    if e.lower() != ".pp3": continue
    allImages.append(dir + "/" + i)
  allImages.sort()
  return allImages


def get_images(dir):
  print("Scanning " + dir)
  allImages = []

  if not os.path.isdir(dir): 
      return allImages

  for i in os.listdir(dir):
    b, e = os.path.splitext(i)
    if e.lower() not in image_extensions: continue
    allImages.append(dir + "/" + i)
  allImages.sort()
  return allImages


base_dir = os.getcwd()

side_cars = get_images_sidecar(base_dir)
print ("Side cars")
for i in side_cars:
    print(i)

meh_images = [ os.path.basename(i).lower() for i in get_images(os.path.join(base_dir, "meh")) ]
good_images = [ os.path.basename(i).lower() for i in get_images(os.path.join(base_dir, "good")) ]
two_star_images = [ os.path.basename(i).lower() for i in get_images(os.path.join(base_dir, "2_star")) ]
three_star_images = [ os.path.basename(i).lower() for i in get_images(os.path.join(base_dir, "3_star")) ]
four_star_images = [ os.path.basename(i).lower() for i in get_images(os.path.join(base_dir, "4_star")) ]
five_star_images = [ os.path.basename(i).lower() for i in get_images(os.path.join(base_dir, "5_star")) ]
#print ("Five stars images")
#for i in three_star_images:
#    print(i)

meh_side_cars = [ sidecar for sidecar in side_cars for image in meh_images if image in sidecar.lower() ]
good_side_cars = [ sidecar for sidecar in side_cars for image in good_images if image in sidecar.lower() ]
two_star_side_cars = [ sidecar for sidecar in side_cars for image in two_star_images if image in sidecar.lower() ]
three_star_side_cars = [ sidecar for sidecar in side_cars for image in three_star_images if image in sidecar.lower() ]
four_star_side_cars = [ sidecar for sidecar in side_cars for image in four_star_images if image in sidecar.lower() ]
five_star_side_cars = [ sidecar for sidecar in side_cars for image in five_star_images if image in sidecar.lower() ]

print ("meh Side cars")
for i in meh_side_cars:
    print(i + " " + os.path.join(base_dir, "meh", os.path.basename(i)))
    os.rename(i, os.path.join(base_dir, "meh", os.path.basename(i)))

print ("good Side cars")
for i in good_side_cars:
    print(i + " " + os.path.join(base_dir, "good", os.path.basename(i)))
    os.rename(i, os.path.join(base_dir, "good", os.path.basename(i)))

print ("Two stars Side cars")
for i in two_star_side_cars:
    print(i + " " + os.path.join(base_dir, "2_star", os.path.basename(i)))
    os.rename(i, os.path.join(base_dir, "2_star", os.path.basename(i)))

print ("Three stars Side cars")
for i in three_star_side_cars:
    print(i + " " + os.path.join(base_dir, "3_star", os.path.basename(i)))
    os.rename(i, os.path.join(base_dir, "3_star", os.path.basename(i)))

print ("Four stars Side cars")
for i in four_star_side_cars:
    print(i + " " + os.path.join(base_dir, "4_star", os.path.basename(i)))
    os.rename(i, os.path.join(base_dir, "4_star", os.path.basename(i)))

print ("Five stars Side cars")
for i in five_star_side_cars:
    print(i + " " + os.path.join(base_dir, "5_star", os.path.basename(i)))
    os.rename(i, os.path.join(base_dir, "5_star", os.path.basename(i)))

